from unsloth import FastModel
import torch
import json
from datasets import Dataset
import os
from unsloth import apply_chat_template

# -----------------------
# Environment Setup
# -----------------------
num_proc = 4
print_example_index = 3

os.environ["OMP_NUM_THREADS"] = str(num_proc)
os.environ["MKL_NUM_THREADS"] = str(num_proc)
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# (Optional) List of available fourbit models for reference.
fourbit_models = [
    "unsloth/gemma-3-1b-it-unsloth-bnb-4bit",
    "unsloth/gemma-3-4b-it-unsloth-bnb-4bit",
    "unsloth/gemma-3-12b-it-unsloth-bnb-4bit",
    "unsloth/gemma-3-27b-it-unsloth-bnb-4bit",
    "unsloth/Llama-3.1-8B",
    "unsloth/Llama-3.2-3B",
    "unsloth/Llama-3.3-70B",
    "unsloth/mistral-7b-instruct-v0.3",
    "unsloth/Phi-4",
]

# -----------------------
# Model and Tokenizer Setup
# -----------------------
model, tokenizer = FastModel.from_pretrained(
    model_name="unsloth/Llama-3.1-8B",
    max_seq_length=2048,
    load_in_4bit=True,
    load_in_8bit=False,
    full_finetuning=False,
    device_map="auto",
    max_memory={0: "40GiB", "cpu": "32GiB"},
    offload_folder="offload",
)

# Apply LoRA adapters (update only a small amount of parameters)
model = FastModel.get_peft_model(
    model,
    finetune_vision_layers=False,
    finetune_language_layers=True,
    finetune_attention_modules=True,
    finetune_mlp_modules=True,
    r=8,
    lora_alpha=8,
    lora_dropout=0,
    bias="none",
    random_state=3407,
)

# -----------------------
# Data Conversion to LLaMA 3.1 Format
# -----------------------

def load_alpaca_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

def alpaca_to_unsloth_format(alpaca_data):
    unsloth_data = []

    for entry in alpaca_data:
        instruction = entry.get("instruction", "").strip()
        input_text = entry.get("input", "").strip()
        output_text = entry.get("output", "").strip()

        user_message = f"{instruction}\n{input_text}" if input_text else instruction

        conversation = [
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": output_text},
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": output_text}
        ]

        unsloth_data.append({"text": conversation})

    return unsloth_data

# Load Alpaca data.
alpaca_data = load_alpaca_jsonl("learning_json/alpaca.jsonl")
print(f"Total loaded entries: {len(alpaca_data)}")

# Convert to unsloth
unsloth_data = alpaca_to_unsloth_format(alpaca_data)
print(f"nsloth data format: {unsloth_data[0]}")



dataset = Dataset.from_list(unsloth_data)
dataset = apply_chat_template(
    dataset,
    tokenizer=tokenizer,
    chat_template="llama-3",
    conversation_extension=2  # Combines two single-turn exchanges into one
)


# -----------------------
# Setup Training with TRL's SFTTrainer
# -----------------------
from trl import SFTTrainer, SFTConfig

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    eval_dataset=None,
    args=SFTConfig(
        dataset_num_proc=num_proc,
        dataset_text_field="text",
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        warmup_steps=5,
        max_steps=250,
        learning_rate=1e-5,
        logging_steps=1,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=3407,
        report_to="none",
    ),
)

# -----------------------
# GPU Memory Stats Before Training
# -----------------------
gpu_stats = torch.cuda.get_device_properties(0)
start_gpu_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
max_memory = round(gpu_stats.total_memory / 1024 / 1024 / 1024, 3)
print(f"GPU = {gpu_stats.name}. Max memory = {max_memory} GB.")
print(f"{start_gpu_memory} GB of memory reserved.")

# -----------------------
# Training
# -----------------------
trainer_stats = trainer.train()

# -----------------------
# Final GPU Memory and Time Stats
# -----------------------
used_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
used_memory_for_training = round(used_memory - start_gpu_memory, 3)
used_percentage = round(used_memory / max_memory * 100, 3)
training_percentage = round(used_memory_for_training / max_memory * 100, 3)
print(f"{trainer_stats.metrics['train_runtime']} seconds used for training.")
print(f"{round(trainer_stats.metrics['train_runtime'] / 60, 2)} minutes used for training.")
print(f"Peak reserved memory = {used_memory} GB.")
print(f"Peak reserved memory for training = {used_memory_for_training} GB.")
print(f"Peak reserved memory % of max memory = {used_percentage} %.")
print(f"Peak reserved memory for training % of max memory = {training_percentage} %.")

# -----------------------
# Save the Model
# -----------------------
model.save_pretrained("models/my-gemma-3")
tokenizer.save_pretrained("models/my-gemma-3")
model.save_pretrained_merged("models/my-gemma-3-finetune-merged", tokenizer)
# Optionally, save gguf format (if supported):
# model.save_pretrained_gguf("models/my-gemma-3-finetune-gguf-q8", quantization_type="Q8_0")

# -----------------------
# Inference
# -----------------------
def llama31_inference_prompt(user_text, 
                             system_text=(
                                 "Environment: ipython\n"
                                 "Tools: brave_search, wolfram_alpha\n"
                                 "Cutting Knowledge Date: December 2023\n"
                                 "Today Date: 23 July 2024\n"
                                 "You are a helpful assistant."
                             )):
    """
    Create an inference prompt in LLaMA 3.1 format using only a user query.
    """
    prompt = (
        "<|begin_of_text|>"
        "<|start_header_id|>system<|end_header_id|>\n"
        f"{system_text}\n"
        "<|eot_id|>"
        "<|start_header_id|>user<|end_header_id|>\n"
        f"{user_text}\n"
        "<|eot_id|>"
        "<|start_header_id|>assistant<|end_header_id|> "
    )
    return prompt

user_query = "Can you help me solve this equation: x^3 - 4x^2 + 6x - 24 = 0?"
inference_text = llama31_inference_prompt(user_query)
print("Inference Prompt:")
print(inference_text)

# Tokenize and generate
inputs = tokenizer([inference_text], return_tensors="pt").to("cuda")
outputs = model.generate(
    **inputs,
    max_new_tokens=500,
    temperature=1.0,
    top_p=0.95,
    top_k=64,
)
decoded_outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)
print("Generated Response:")
print(decoded_outputs[0])
