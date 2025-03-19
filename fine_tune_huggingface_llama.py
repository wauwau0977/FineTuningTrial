import torch
import logging
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, Trainer, TrainingArguments, DataCollatorForSeq2Seq
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
import os

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

# Prepare for k-bit training
model = prepare_model_for_kbit_training(model)
model.config.use_cache = False
model.config.pretraining_tp = 1

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

logger.info("Model and tokenizer loaded successfully.")

# -----------------------
# Load and Format Dataset (Alpaca Style)
# -----------------------
logger.info("Loading dataset...")
dataset = load_dataset("json", data_files="learning_json/alpaca.jsonl")["train"]
dataset = dataset.train_test_split(test_size=0.1, seed=42)
logger.info(f"Dataset split into train ({len(dataset['train'])}) and test ({len(dataset['test'])})")

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

# --- Robust Column Removal ---
for split in ["train", "test"]:
    columns_to_remove = ["instruction", "input", "output"]
    existing_columns = dataset[split].column_names
    columns_to_remove = [col for col in columns_to_remove if col in existing_columns]
    dataset[split] = dataset[split].map(format_alpaca, remove_columns=columns_to_remove)

logger.info(f"First formatted training example: {dataset['train'][0]}")

# -----------------------
# Apply LoRA
# -----------------------
logger.info("Applying LoRA configuration...")
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    lora_dropout=0.1,
    task_type="CAUSAL_LM",
    bias="none",
    target_modules=[
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
        "gate_proj",
        "up_proj",
        "down_proj",
    ],
)

model = get_peft_model(model, lora_config)
logger.info("LoRA applied to model.")
model.print_trainable_parameters()

# -----------------------
# Tokenization
# -----------------------

def tokenize_and_format(examples):
    formatted_texts = []

    for messages in examples["messages"]:
        formatted_text = tokenizer.apply_chat_template(messages, tokenize=False)
        formatted_texts.append(formatted_text)

    tokenized_inputs = tokenizer(
        formatted_texts,
        padding="max_length",
        truncation=True,
        max_length=512,
        return_tensors="pt"
    )

    tokenized_inputs["labels"] = tokenized_inputs["input_ids"].clone()
    return tokenized_inputs

# -----------------------
# Training Arguments
# -----------------------
logger.info("Setting up training arguments...")

output_dir = "./outputs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


training_args = TrainingArguments(
    output_dir=output_dir,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    num_train_epochs=10,
    learning_rate=2e-5,
    weight_decay=0.01,
    fp16=True,
    logging_steps=1,
    save_strategy="epoch",
    save_total_limit=2,
    optim="adamw_torch",
    dataloader_num_workers=4,
    gradient_checkpointing=True,
    evaluation_strategy="steps",
    eval_steps=1,
    do_eval=True,
)

# -----------------------
# Trainer
# -----------------------
logger.info("Initializing `Trainer`...")
data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model, padding=True)

trainer = Trainer(
    model=model,  # Pass the model to the Trainer
    args=training_args,
    train_dataset=dataset["train"].map(tokenize_and_format, batched=True, remove_columns=["messages"], num_proc=4),
    eval_dataset=dataset["test"].map(tokenize_and_format, batched=True, remove_columns=["messages"], num_proc=4),
    data_collator=data_collator,
)

logger.info("Starting training...")
trainer.train()
logger.info("Training completed.")

# -----------------------
# Save Model  (Only save after training)
# -----------------------
logger.info("Saving fine-tuned model...")
final_model_dir = "models/my-llama3-finetuned"
model.save_pretrained(final_model_dir)  # Save the *trained* model
tokenizer.save_pretrained(final_model_dir)
logger.info("Fine-tuning complete! Model saved successfully.")

# -----------------------
# Inference (Use the trained model directly)
# -----------------------

logger.info("Starting inference...")

#  NO model loading here. We use the 'model' from training.

# Move model to GPU if available (important to do this *after* LoRA)
if torch.cuda.is_available():
    model = model.to("cuda")  # Move the *trained* model

# Set model to evaluation mode
model.eval()

# Define questions
questions = [
    "What is the capital of France?",
    "What means Kräsemäse in Glattfelderisch?",
    "'Jaudihaudi Jo' in Glattfelden Switzerland what does that mean?",
]

for question in questions:
    messages = [{"role": "user", "content": question}]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt")

    if torch.cuda.is_available():
        inputs = {k: v.to("cuda") for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=150, do_sample=True, top_k=50, top_p=0.95)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Question: {question}")
    print(f"Answer: {response}\n")

logger.info("Inference complete.")