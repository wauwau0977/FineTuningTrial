from unsloth import FastModel
import torch
import json
from datasets import Dataset
import os


num_proc = 4
print_example_index = 3

os.environ["OMP_NUM_THREADS"] = str(num_proc)  # Change '4' to the desired number of CPU cores
os.environ["MKL_NUM_THREADS"] = str(num_proc)  # Also limit MKL-based parallelism
os.environ["TOKENIZERS_PARALLELISM"] = "false"  # Prevent Hugging Face tokenizer from spawning many processes

fourbit_models = [
    # 4bit dynamic quants for superior accuracy and low memory use
    "unsloth/gemma-3-1b-it-unsloth-bnb-4bit",
    "unsloth/gemma-3-4b-it-unsloth-bnb-4bit",
    "unsloth/gemma-3-12b-it-unsloth-bnb-4bit",
    "unsloth/gemma-3-27b-it-unsloth-bnb-4bit",

    # Other popular models!
    "unsloth/Llama-3.1-8B",
    "unsloth/Llama-3.2-3B",
    "unsloth/Llama-3.3-70B",
    "unsloth/mistral-7b-instruct-v0.3",
    "unsloth/Phi-4",
] # More models at https://huggingface.co/unsloth

model, tokenizer = FastModel.from_pretrained(
    model_name = "unsloth/gemma-3-4b-it",
    max_seq_length = 2048, # Choose any for long context!
    load_in_4bit = True,  # 4 bit quantization to reduce memory
    load_in_8bit = False, # [NEW!] A bit more accurate, uses 2x memory
    full_finetuning = False, # [NEW!] We have full finetuning now!
    # token = "hf_...", # use one if using gated models
    device_map="auto",         # Automatically place model parts on devices
    max_memory={0: "40GiB", "cpu": "32GiB"},  # Limit memory per device
    offload_folder="offload",   # Offload model weights to disk if needed
    # not helping! attn_implementation='eager'  # TODO: Actually not so sure if good or not... at least it warns if not set!!! https://github.com/unslothai/unsloth/issues/2025
)

# We now add LoRA adapters so we only need to update a small amount of parameters!
model = FastModel.get_peft_model(
    model,
    finetune_vision_layers     = True, # HACK, TODO, allow load? Turn off for just text!
    finetune_language_layers   = True,  # Should leave on!
    finetune_attention_modules = True,  # Attention good for GRPO
    finetune_mlp_modules       = True,  # SHould leave on always!

    r = 8,           # Larger = higher accuracy, but might overfit
    lora_alpha = 8,  # Recommended alpha == r at least
    lora_dropout = 0,
    bias = "none",
    random_state = 3407,
)

# TARGET SPEC FORMAT
# <bos><start_of_turn>user
# Hello!<end_of_turn>
# <start_of_turn>model
# Hey there!<end_of_turn>

from unsloth.chat_templates import get_chat_template
tokenizer = get_chat_template(
    tokenizer,
    chat_template = "gemma-3",
)

print("Tokenizer-Chat-Template: " +tokenizer.chat_template)


from datasets import load_dataset
# Load local alpaca.jsonl file
def load_alpaca_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

alpaca_data = load_alpaca_jsonl("learning_json/alpaca.jsonl")
print(f"Total loaded entries: {len(alpaca_data)}")  # ✅ Ensure data is loaded properly


def convert_alpaca_to_gemma(alpaca_data):
    gemma_data = []
    
    for entry in alpaca_data:
        # Get and clean the fields
        instruction = entry.get("instruction", "").strip()
        input_text = entry.get("input", "").strip()
        output_text = entry.get("output", "").strip()

        # Concatenate instruction and input if input exists
        user_message = f"{instruction}\n{input_text}" if input_text else instruction

        # Build a structured conversation without any special tokens.
        # The chat template later will add the necessary formatting tokens.
        conversation = [
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": output_text}
        ]
        
        gemma_data.append({"text": conversation})
    
    return gemma_data

# Load Alpaca data as before
alpaca_data = load_alpaca_jsonl("learning_json/alpaca.jsonl")
print(f"Total loaded entries: {len(alpaca_data)}")  # Should match number of lines

# Convert data using the new conversion function
converted_data = convert_alpaca_to_gemma(alpaca_data)
print("Converted Data Example:", converted_data[print_example_index])

# Create the dataset (each item already has a 'text' field with the conversation structure)
dataset = Dataset.from_list(converted_data)

# Standardize the data formats (if needed by your finetuning procedure)
from unsloth.chat_templates import standardize_data_formats
dataset = standardize_data_formats(dataset)

# Apply the chat template to add the correct tokens
def apply_chat_template(examples):
    texts = tokenizer.apply_chat_template(examples["text"])
    return {"text": texts}

dataset = dataset.map(apply_chat_template, batched=True, num_proc=4 )
print(dataset[min(print_example_index, len(dataset) - 1)]["text"])




# Now let's use Huggingface TRL's SFTTrainer! More docs here: TRL SFT docs. We do 60 steps to speed things up, but you can set num_train_epochs=1 for a full run, and turn off max_steps=None.
from trl import SFTTrainer, SFTConfig
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    eval_dataset = None, # Can set up evaluation!
    args = SFTConfig(
        dataset_num_proc=num_proc, # limit number of processes for tokenization... goes way beyond on cloud CPU
        dataset_text_field = "text",
        per_device_train_batch_size = 2, # 2 for Medium memory GPU (<= 16GB)
        gradient_accumulation_steps = 4, # Use GA to mimic batch size!
        warmup_steps = 5,
        # num_train_epochs = 1, # Set this for 1 full training run.
        max_steps = 250,
        learning_rate = 1e-5, # Reduce to 2e-5 for long training runs
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        report_to = "none", # Use this for WandB etc
    ),
)


# We also use Unsloth's train_on_completions method to only train on the assistant outputs and ignore the loss on the user's inputs. This helps increase accuracy of finetunes!
from unsloth.chat_templates import train_on_responses_only
trainer = train_on_responses_only(
    trainer,
    instruction_part = "<start_of_turn>user\n",
    response_part = "<start_of_turn>model\n",
)

#  textLet's verify masking the instruction part is done! Let's print the 100th row again:
dMasking = tokenizer.decode(trainer.train_dataset[print_example_index]["input_ids"])
print(f"debug masking: {dMasking}")


# Now let's print the masked out example - you should see only the answer is present:
dAnswer = tokenizer.decode([tokenizer.pad_token_id if x == -100 else x for x in trainer.train_dataset[print_example_index]["labels"]]).replace(tokenizer.pad_token, " ")
print(f"debug answer: {dAnswer}")

# memory stats
gpu_stats = torch.cuda.get_device_properties(0)
start_gpu_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
max_memory = round(gpu_stats.total_memory / 1024 / 1024 / 1024, 3)
print(f"GPU = {gpu_stats.name}. Max memory = {max_memory} GB.")
print(f"{start_gpu_memory} GB of memory reserved.")

# now really train
trainer_stats = trainer.train()



# @title Show final memory and time stats
used_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
used_memory_for_lora = round(used_memory - start_gpu_memory, 3)
used_percentage = round(used_memory / max_memory * 100, 3)
lora_percentage = round(used_memory_for_lora / max_memory * 100, 3)
print(f"{trainer_stats.metrics['train_runtime']} seconds used for training.")
print(
    f"{round(trainer_stats.metrics['train_runtime']/60, 2)} minutes used for training."
)
print(f"Peak reserved memory = {used_memory} GB.")
print(f"Peak reserved memory for training = {used_memory_for_lora} GB.")
print(f"Peak reserved memory % of max memory = {used_percentage} %.")
print(f"Peak reserved memory for training % of max memory = {lora_percentage} %.")



# SAVE MODEL
model.save_pretrained("models/my-gemma-3")  # Local saving
tokenizer.save_pretrained("models/my-gemma-3")

# save merged
model.save_pretrained_merged("models/my-gemma-3-finetune-merged", tokenizer)

# save gguf
# model.save_pretrained_gguf(
#         "models/my-gemma-3-finetune-gguf-q8",
#         quantization_type = "Q8_0", # For now only Q8_0, BF16, F16 supported
# )


# inference
from unsloth.chat_templates import get_chat_template
tokenizer = get_chat_template(
    tokenizer,
    chat_template = "gemma-3",
)
messages = [{
    "role": "user",
    "content": [{
        "type" : "text",
        "text" : "Was bedeuten die Wörter 'Cheibegruusig' und 'Sausiwegbini Jo' in Glattfelden (Schweiz)?",
    }]
}]
text = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt = True, # Must add for generation
)
outputs = model.generate(
    **tokenizer([text], return_tensors = "pt").to("cuda"),
    max_new_tokens = 500, # Increase for longer outputs!
    # Recommended Gemma-3 settings!
    temperature = 1.0, top_p = 0.95, top_k = 64,
)
tokenizer.batch_decode(outputs)

decoded_outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True) #add skip special tokens
print(decoded_outputs[0])  # Print the first (and only) decoded result