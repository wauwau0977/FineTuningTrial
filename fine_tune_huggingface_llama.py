# Install required libraries (if not installed)
# !pip install transformers peft torch accelerate datasets bitsandbytes

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from datasets import load_dataset
from peft import LoraConfig, get_peft_model
from transformers import TrainingArguments, Trainer, DataCollatorForLanguageModeling

# -----------------------
# Load Model & Tokenizer with 4-bit Quantization
# -----------------------
model_name = "NousResearch/Meta-Llama-3.1-8B-Instruct"

# Define the quantization configuration
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,              # Enable 4-bit quantization
    bnb_4bit_quant_type="nf4",      # Set quantization data type to NF4
    bnb_4bit_compute_dtype=torch.bfloat16  # Use bfloat16 for computation
)

# Load the model with the quantization configuration
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config,  # Apply the quantization config
    device_map="auto"  # Auto-distribute across available GPUs
)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # Ensure proper padding

# -----------------------
# Load and Format Dataset (Alpaca Style)
# -----------------------
# Load dataset
dataset = load_dataset("json", data_files="learning_json/alpaca.jsonl")["train"]

# Ensure dataset has both "train" and "test" splits
dataset = dataset.train_test_split(test_size=0.1, seed=42)

# Function to format data properly
def format_alpaca(example):
    instruction = example.get("instruction", "").strip()
    input_text = example.get("input", "").strip()
    output_text = example.get("output", "").strip()
    
    user_message = f"{instruction}\n{input_text}" if input_text else instruction
    formatted_text = f"user: {user_message}\nassistant: {output_text}"
    
    return {"text": formatted_text}

# Apply formatting function
dataset = dataset.map(format_alpaca, remove_columns=dataset["train"].column_names)

# Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Define data collator for efficient batching
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# -----------------------
# Apply LoRA (Low-Rank Adaptation)
# -----------------------
lora_config = LoraConfig(
    r=8,               # Low-rank dimension
    lora_alpha=16,     # Scaling factor
    lora_dropout=0.1,  # Dropout for better generalization
    task_type="CAUSAL_LM"
)

# Apply LoRA to model
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()  # Verify trainable params

# -----------------------
# Set Training Arguments
# -----------------------
training_args = TrainingArguments(
    output_dir="models/my-llama3",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    num_train_epochs=3,
    logging_steps=10,
    save_strategy="epoch",
    save_total_limit=2,
    learning_rate=2e-5,
    weight_decay=0.01,
    fp16=True,  # Use mixed precision for faster training
    report_to="none",
    optim="adamw_torch"  # Use PyTorch's AdamW optimizer
)

# -----------------------
# Train the Model
# -----------------------
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
    data_collator=data_collator
)

trainer.train()

# -----------------------
# Save Fine-Tuned Model
# -----------------------
model.save_pretrained("models/my-llama3-finetuned")
tokenizer.save_pretrained("models/my-llama3-finetuned")
