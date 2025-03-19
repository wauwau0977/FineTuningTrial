import json
import os
import torch
from datasets import Dataset
from unsloth import FastModel
from unsloth.chat_templates import get_chat_template, standardize_data_formats, train_on_responses_only
from trl import SFTTrainer, SFTConfig

# ✅ **Settings**
NUM_PROC = 4
os.environ["OMP_NUM_THREADS"] = str(NUM_PROC)
os.environ["MKL_NUM_THREADS"] = str(NUM_PROC)
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# 📂 **File Path**
ALPACA_JSONL_FILE = "learning_json/alpaca.jsonl"

# ✅ **Step 1: Load Alpaca JSONL File**
def load_alpaca_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

# ✅ **Step 2: Convert Alpaca Format → Unsloth Chat Format**
def convert_alpaca_to_unsloth(alpaca_data):
    formatted_data = []
    
    for entry in alpaca_data:
        instruction = entry.get("instruction", "").strip()
        input_text = entry.get("input", "").strip()
        output_text = entry.get("output", "").strip()

        # Combine instruction & input (if present)
        user_message = f"{instruction}\n{input_text}" if input_text else instruction

        # Convert to Unsloth chat format
        conversation = [
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": output_text}
        ]
        
        formatted_data.append({"text": conversation})
    
    return formatted_data

# ✅ **Load and Convert Dataset**
alpaca_data = load_alpaca_jsonl(ALPACA_JSONL_FILE)
formatted_data = convert_alpaca_to_unsloth(alpaca_data)

# ✅ **Step 3: Create Dataset**
dataset = Dataset.from_list(formatted_data)
dataset = standardize_data_formats(dataset)  # Ensure Unsloth format

# ✅ **Step 4: Load Model & Tokenizer (Llama 3.1)**
model, tokenizer = FastModel.from_pretrained(
    model_name="unsloth/Llama-3.1-8B",
    max_seq_length=2048,  
    load_in_4bit=True,
    load_in_8bit=False,
    full_finetuning=False,
    device_map="auto",
)

# Apply correct chat format for Unsloth
tokenizer = get_chat_template(tokenizer, chat_template="llama-3")

# ✅ **Step 5: Apply Chat Formatting**
def apply_chat_template(examples):
    texts = tokenizer.apply_chat_template(examples["text"])
    return {"text": texts}

dataset = dataset.map(apply_chat_template, batched=True, num_proc=NUM_PROC)

# ✅ **Step 6: Prepare LoRA Fine-tuning**
model = FastModel.get_peft_model(
    model,
    finetune_language_layers=True,
    finetune_attention_modules=True,
    finetune_mlp_modules=True,
    r=8,          
    lora_alpha=8,  
    lora_dropout=0,
    bias="none",
    random_state=3407,
)

# ✅ **Step 7: Configure Training**
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    args=SFTConfig(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        max_steps=500,  # 🔹 Adjust as needed
        learning_rate=1e-5,
        logging_steps=1,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=3407,
        report_to="none",
    ),
)

# ✅ **Step 8: Train ONLY on Model Responses (Boost Accuracy)**
trainer = train_on_responses_only(
    trainer,
    instruction_part="<start_of_turn>user\n",
    response_part="<start_of_turn>model\n",
)

# ✅ **Step 9: Start Training**
trainer.train()

# ✅ **Step 10: Save Model**
SAVE_DIR = "models/my-llama-3-finetune"
model.save_pretrained(SAVE_DIR)
tokenizer.save_pretrained(SAVE_DIR)

# ✅ **(Optional) Merge & Save**
model.save_pretrained_merged(f"{SAVE_DIR}-merged", tokenizer)
