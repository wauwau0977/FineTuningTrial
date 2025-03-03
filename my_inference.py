import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-6.7b-instruct", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/deepseek-coder-6.7b-instruct",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16
).cuda()

# List of prompts
prompts = [
    "Write a quick sort algorithm in Python.",
    "Explain the concept of polymorphism in object-oriented programming.",
    "How does the Python GIL affect multithreading?",
    # Add more prompts as needed
]

# Function to generate response for a given prompt
def generate_response(prompt):
    messages = [{'role': 'user', 'content': prompt}]
    inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
    outputs = model.generate(
        inputs['input_ids'],
        max_new_tokens=512,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.pad_token_id,
        attention_mask=inputs['attention_mask']
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Iterate over prompts and generate responses
responses = {}
for prompt in prompts:
    response = generate_response(prompt)
    responses[prompt] = response
    print(f"Prompt: {prompt}\nResponse: {response}\n{'-'*80}")

# Optionally, save responses to a file
with open("responses.txt", "w") as f:
    for prompt, response in responses.items():
        f.write(f"Prompt: {prompt}\nResponse: {response}\n{'-'*80}\n")
