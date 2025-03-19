import torch
import logging
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling,
    EarlyStoppingCallback,
)
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
import os

# -----------------------
# Debug Logging Setup
# -----------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Starting fine-tuning...")

# -----------------------
# Load Model & Tokenizer with 4-bit Quantization
# -----------------------
model_name = "NousResearch/Meta-Llama-3.1-8B-Instruct"

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True
)

logger.info("Loading model and tokenizer...")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config,
    device_map="auto"
)

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

logger.info(f"Model loaded on device: {model.device}")

# -----------------------
# Load and Format Dataset
# -----------------------
dataset = load_dataset("json", data_files="learning_json/alpaca.jsonl")["train"]
dataset = dataset.train_test_split(test_size=0.1, seed=42)

logger.info(f"Dataset train size: {len(dataset['train'])}, test size: {len(dataset['test'])}")

def format_alpaca(example):
    instruction = example.get("instruction", "").strip()
    input_text = example.get("input", "").strip()
    output_text = example.get("output", "").strip()
    user_message = f"{instruction}\n{input_text}" if input_text else instruction
    return {
        "messages": [
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": output_text}
        ]
    }

for split in ["train", "test"]:
    dataset[split] = dataset[split].map(
        format_alpaca,
        remove_columns=[col for col in ["instruction", "input", "output"] if col in dataset[split].column_names]
    )

# -----------------------
# LoRA and k-bit setup
# -----------------------
logger.info("Applying LoRA configuration...")
lora_config = LoraConfig(
    r=16,
    lora_alpha=32, # twice value of r
    lora_dropout=0.05,
    task_type="CAUSAL_LM",
    bias="none",
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ],
)

# Correct order: first prepare model, then apply LoRA
model = prepare_model_for_kbit_training(model)
model.config.use_cache = False
model.config.pretraining_tp = 1

model = get_peft_model(model, lora_config)

model.print_trainable_parameters()


# -----------------------
# Tokenization
# -----------------------
def tokenize_and_format(examples):
    formatted_texts = [
        tokenizer.apply_chat_template(msg, tokenize=False)
        for msg in examples["messages"]
    ]
    tokenized_inputs = tokenizer(
        formatted_texts,
        padding="max_length",
        truncation=True,
        max_length=512
    )
    tokenized_inputs["labels"] = tokenized_inputs["input_ids"].copy()
    return tokenized_inputs

# -----------------------
# Training Arguments
# -----------------------
training_args = TrainingArguments(
    output_dir="./outputs",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    #num_train_epochs=50,
    max_steps=1000,
    learning_rate=5e-5,
    weight_decay=0.01,
    fp16=True,
    logging_steps=1,
    save_strategy="epoch",
    save_total_limit=2,
    optim="adamw_torch",
    dataloader_num_workers=4,
    gradient_checkpointing=True,
    eval_strategy="epoch",
    eval_steps=2,
    do_eval=True,
    label_names=["labels"],  # Explicitly set the label names
    greater_is_better=False,      # Lower eval_loss is better
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
)

# -----------------------
# Trainer
# -----------------------
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"].map(tokenize_and_format, batched=True, remove_columns=["messages"], num_proc=4),
    eval_dataset=dataset["test"].map(tokenize_and_format, batched=True, remove_columns=["messages"], num_proc=4),
    data_collator=data_collator,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=5)],
)

logger.info("Starting training...")
trainer.train()

# -----------------------
# Save Model
# -----------------------
model.save_pretrained("models/my-llama3-finetuned")
tokenizer.save_pretrained("models/my-llama3-finetuned")


# Merge LoRA and save the merged model
merged_model = model.merge_and_unload()
merged_model.save_pretrained("models/my-llama3-finetuned-merged")
tokenizer.save_pretrained("models/my-llama3-finetuned-merged")


# -----------------------
# Inference
# -----------------------
model.eval()
device = model.device

questions = [
    "What is the capital of France?",
    "What means Kräsemäse in Glattfelderisch?",
    "'Jaudihaudi Jo' in Glattfelden Switzerland what does that mean?",
    "In Glattfelderisch say 'super cool'.",
    "In Glattfelden, Switzerland, what language do they use?",  # Rephrased
    "What means the word 'Cheibegruusig' in Glattfelden (Switzerland)", # REVERSE LOGIC
    "Was heisst 'Cheibegruusig' in Glattfelderisch?", # REVERSE LOGIC and LANGUAGE SWITCH
    "In Glattfelder-Schweizer-Deutsch what means 'Sausiwegbini Jo'?", # REVERSE
]

# Store prompts, responses, and timings
results = []

for question in questions:
    messages = [{"role": "user", "content": question}]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        start_time = torch.cuda.Event(enable_timing=True) # more precise than time.time()
        end_time = torch.cuda.Event(enable_timing=True)
        start_time.record()
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7,
            repetition_penalty=1.2,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id
        )
        end_time.record()
        torch.cuda.synchronize() # Wait for the events to be recorded!
        elapsed_time_ms = start_time.elapsed_time(end_time) # measure time

    response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    print(f"Question: {question}")
    print(f"Answer: {response}")
    print(f"-------------------------------------------------------- {elapsed_time_ms:.2f} ms\n")

    results.append((question, prompt, response, elapsed_time_ms))


print("\nPrompts:")
for _, prompt, _, _ in results:
    print(prompt)

logger.info("Inference complete.")

