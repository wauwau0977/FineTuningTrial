# Install required libraries (if not installed)
# !pip install transformers peft torch accelerate datasets bitsandbytes

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from datasets import load_dataset
from peft import LoraConfig, get_peft_model
from transformers import TrainingArguments, Trainer

# -----------------------
# Load Model & Tokenizer (4-bit)
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


tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # Ensure proper padding

# -----------------------
# Load and Format Dataset (Alpaca Style)
# -----------------------
dataset = load_dataset("json", data_files="learning_json/alpaca.jsonl")

# Ensure dataset is structured correctly
if "train" not in dataset:
    dataset = dataset["train_test_split"]["train"]  # Use full dataset if no explicit "train"

# Function to format data properly
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

dataset = dataset.map(format_alpaca)

# Apply chat template correctly
dataset = dataset.map(lambda x: {"text": tokenizer.apply_chat_template(x["messages"], tokenize=False)})

# -----------------------
# Apply LoRA (Low-Rank Adaptation)
# -----------------------
lora_config = LoraConfig(
    r=8,               # Low-rank dimension
    lora_alpha=16,     # Scaling factor
    lora_dropout=0.1,  # Dropout for better generalization
    task_type="CAUSAL_LM"
)

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
    fp16=True,
    report_to="none",
    optim="adamw_hf"
)

# -----------------------
# Train the Model
# -----------------------
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,  # Remove ["train"] to avoid KeyErrors
    tokenizer=tokenizer
)

trainer.train()

# -----------------------
# Save Fine-Tuned Model
# -----------------------
model.save_pretrained("models/my-llama3-finetuned")
tokenizer.save_pretrained("models/my-llama3-finetuned")
