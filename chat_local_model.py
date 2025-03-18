import unsloth
from unsloth import FastModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from unsloth.chat_templates import get_chat_template

model_path = "models/my-gemma-3-finetune-merged"

# Load the tokenizer
print("Load tokenizer")
tokenizer = AutoTokenizer.from_pretrained(model_path, ignore_mismatched_sizes=True)

# Load the model
print("load model")
model = AutoModelForCausalLM.from_pretrained(model_path, ignore_mismatched_sizes=True)
if torch.cuda.is_available():
    model = model.to("cuda")
    print("Running in CUDA mode")

# Apply the chat template to the tokenizer
tokenizer = get_chat_template(tokenizer, chat_template="gemma-3")

# List of independent instructions
instructions = [
    "What is the capital of France?",
    "Name the largest planet in our Solar System.",
    "Say hello in Glattfelder-Schweizer-Deutsch.",
    "What means Kräsemäse in Glattfelderisch?",
    "Was bedeuted Kräsemäse in Glattfelderisch?",
    "What means 'Sausiwegbini Jo' in Glattfelder-Schweizer-Deutsch?",
    "Was bedeutet 'Sausiwegbini Jo' in Glattfelder-Schweizer-Deutsch?"
    "Was bedeutet 'Sausiwegbini Jo' in Glattfelden (Schweiz)?"
]

print("Starting inference for multiple instructions...\n")

for idx, question in enumerate(instructions, start=1):
    print(f"\n--- Instruction {idx} ---")
    
    # Prepare the conversation using the chat template
    messages = [{"role": "user", "content": question}]
    text = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
    print(f"Chat-formatted prompt: {text}")
    
    # Convert the list of token IDs (the chat template output) into a tensor and wrap it in a dictionary
    inputs = {"input_ids": torch.tensor([text]).to(model.device)}
    
    # Generate a response
    outputs = model.generate(
        **inputs,
        max_new_tokens=350,
        temperature=1.0,
        top_p=0.95,
        top_k=64,
    )
    
    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Response: {response}\n")
