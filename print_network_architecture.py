import torch
from transformers import AutoModelForCausalLM

# Select the model (change this to any Hugging Face model)
MODEL_NAME = "NousResearch/Hermes-3-Llama-3.2-3B"  # Example: "gpt2", "bert-base-uncased"

# Load the model
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,  # Use float16 to reduce memory usage
    device_map="cpu"  # Change to "auto" for GPU
)

# Print all layers with full hierarchy
print("\n🔍 **Full Model Architecture:**\n")
for name, layer in model.named_modules():
    print(f"{name} -> {layer}")

print("\n✅ Model layers printed successfully!")
