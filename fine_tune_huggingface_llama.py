# Install required libraries (if not installed)
# !pip install transformers peft torch accelerate datasets bitsandbytes

import torch
import logging
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from datasets import load_dataset
from peft import LoraConfig, get_peft_model
from transformers import TrainingArguments, Trainer, DataCollatorForLanguageModeling

# -----------------------
# Debug Logging Setup
# -----------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Starting the fine-tuning script...")

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
logger.info("Loading model and tokenizer...")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config,  # Apply the quantization config
    device_map="auto"  # Auto-distribute across available GPUs
)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # Ensure proper padding

logger.info("Model and tokenizer loaded successfully.")

# -----------------------
# Load and Format Dataset (Alpaca Style)
# -----------------------
logger.info("Loading dataset...")
dataset = load_dataset("json", data_files="learning_json/alpaca.jsonl")["train"]

# Ensure dataset has both "train" and "test" splits
dataset = dataset.train_test_split(test_size=0.1, seed=42)
logger.info(f"Dataset split into train ({len(dataset['train'])}) and test ({len(dataset['test'])})")

# Function to format data properly
def format_alpaca(example):
    instruction = example.get("instruction", "").strip()
    input_text = example.get("input", "").strip()
    output_text = example.get("output", "").strip()
    
    user_message = f"{instruction}\n{input_text}" if input_text else instruction
    formatted_text = f"user: {user_message}\nassistant: {output_text}"
    
    return {"text": formatted_text}

logger.info("Applying formatting function to dataset...")
dataset = dataset.map(format_alpaca, remove_columns=dataset["train"].column_names)

# Debug: Print first formatted example
logger.info(f"First formatted training example: {dataset['train'][0]}")

# Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512)

logger.info("Tokenizing dataset...")
tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Debug: Print first tokenized example
logger.info(f"First tokenized training example: {tokenized_datasets['train'][0]}")

# Define data collator for efficient batching
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# -----------------------
# Apply LoRA (Low-Rank Adaptation)
# -----------------------
logger.info("Applying LoRA configuration...")
lora_config = LoraConfig(
    r=8,               # Low-rank dimension
    lora_alpha=16,     # Scaling factor
    lora_dropout=0.1,  # Dropout for better generalization
    task_type="CAUSAL_LM"
)

# Apply LoRA to model
model = get_peft_model(model, lora_config)
logger.info("LoRA applied to model.")
model.print_trainable_parameters()  # Verify trainable params

# -----------------------
# Set Training Arguments
# -----------------------
logger.info("Setting up training arguments...")
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
logger.info("Initializing trainer...")
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
    data_collator=data_collator
)

logger.info("Starting training...")
trainer.train()
logger.info("Training completed.")

# -----------------------
# Save Fine-Tuned Model
# -----------------------
logger.info("Saving fine-tuned model...")
model.save_pretrained("models/my-llama3-finetuned")
tokenizer.save_pretrained("models/my-llama3-finetuned")

logger.info("Fine-tuning complete! Model saved successfully.")
