import unsloth
from unsloth import FastModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from unsloth.chat_templates import get_chat_template

model_path = "models/my-gemma-3-finetune-merged"

# Load the tokenizer
print("load tokenizer")
tokenizer = AutoTokenizer.from_pretrained(model_path, ignore_mismatched_sizes=True)

# Load the model
print("load model")
model = AutoModelForCausalLM.from_pretrained(model_path, ignore_mismatched_sizes=True)


# Apply chat template to get tokenized prompt (as a list of IDs)
print("About to tokenize input")
question = "What is the capital of France?"
messages = [{"role": "user", "content": question}]
text = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
print(f"text chat-template: {text}")

# Convert list of token IDs into a tensor and wrap in a dict with key "input_ids"
inputs = {"input_ids": torch.tensor([text]).to(model.device)}
print("Text tokenized. Inputs:", inputs)

# Generate response
outputs = model.generate(
    **inputs,
    max_new_tokens=128,
    temperature=1.0,
    top_p=0.95,
    top_k=64,
)

# Decode and print the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Model Response:", response)