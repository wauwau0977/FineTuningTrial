from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import time

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-6.7b-instruct", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/deepseek-coder-6.7b-instruct",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16
).cuda()

# Define a list of prompts including Python and Java examples
prompts = [
    "write a quick sort algorithm in python.",
    "explain how to implement a binary search in python.",
    "write a function that calculates factorial in python.",
    "write a quick sort algorithm in java.",
    "explain how to implement a binary search in java."
]

# Loop through each prompt, generate output and measure inference time
for prompt in prompts:
    messages = [{'role': 'user', 'content': prompt}]

    start_time = time.time()

    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)
    
    outputs = model.generate(
        inputs,
        max_new_tokens=512,
        do_sample=False,
        top_k=50,
        top_p=0.95,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id
    )
    end_time = time.time()
    inference_time = end_time - start_time

    # Decode the output, skipping the tokens corresponding to the input prompt
    output_text = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True)
    
    print(f"Prompt: {prompt}")
    print("Generated Output:")
    print(output_text)
    print(f"Inference time: {inference_time:.2f} seconds")
    print("=" * 50)
