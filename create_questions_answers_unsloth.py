from unsloth import FastModel
from unsloth.chat_templates import get_chat_template
import time
import torch

fourbit_models = [
    # 4bit dynamic quants for superior accuracy and low memory use
    "unsloth/gemma-3-1b-it-unsloth-bnb-4bit",
    "unsloth/gemma-3-4b-it-unsloth-bnb-4bit",
    "unsloth/gemma-3-12b-it-unsloth-bnb-4bit",
    "unsloth/gemma-3-27b-it-unsloth-bnb-4bit",

    # Other popular models!
    "unsloth/Llama-3.1-8B",
    "unsloth/Llama-3.2-3B",
    "unsloth/Llama-3.3-70B",
    "unsloth/mistral-7b-instruct-v0.3",
    "unsloth/Phi-4",
] # More models at https://huggingface.co/unsloth

initial_gpu_allocated = torch.cuda.memory_allocated() / (1024**3)
initial_gpu_reserved = torch.cuda.memory_reserved() / (1024**3)

model, tokenizer = FastModel.from_pretrained(
    model_name = "unsloth/gemma-3-27b-it",
    max_seq_length = 128000,  # max sequence size for Gemma 3 is 128k probably 131072, but we go for 128
    load_in_4bit = True,  # 4-bit quantization for lower memory usage
)

tokenizer = get_chat_template(
    tokenizer,
    chat_template = "gemma-3",
)

questions = [
    "Continue the sequence: 1, 1, 2, 3, 5, 8,",
    "What is the capital of France?",
    "Explain the theory of relativity briefly.",
    "What is the tallest mountain on Earth?",
    "Translate 'hello' into German.",
    "What is quantum computing?",
    "List three famous novels by Charles Dickens.",
    "Summarize the plot of Hamlet.",
    "What is the chemical symbol for gold?",
    "Who invented the telephone?",
]

for question in questions:

    start_time = time.time()

    messages = [{
        "role": "user",
        "content": [{
            "type": "text",
            "text": question,
        }]
    }]

    text = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
    )

    inputs = tokenizer([text], return_tensors="pt").to("cuda")
    input_len = inputs.input_ids.shape[1]

    outputs = model.generate(
        **inputs,
        max_new_tokens=8000,
        temperature=1.0,
        top_p=0.95,
        top_k=64,
    )

    end_time = time.time()

    generation_time = end_time - start_time

      # Decode the generated tokens, excluding the input prompt
    decoded = tokenizer.batch_decode(outputs[:, input_len:], skip_special_tokens=True)

    print(f"Q: {question}\n")
    print(f"A: {decoded[0]}\n")
    print(f"Generation time: {generation_time:.2f} seconds\n")
    print("-" * 80, "\n")



# GPU memory usage after queries
final_gpu_allocated = torch.cuda.memory_allocated() / (1024**3)
final_gpu_reserved = torch.cuda.memory_reserved() / (1024**3)

print(f"Initial GPU allocated memory: {initial_gpu_allocated:.2f} GB")
print(f"Initial GPU reserved memory: {initial_gpu_reserved:.2f} GB")
print(f"Final GPU allocated memory: {final_gpu_allocated:.2f} GB")
print(f"Final GPU reserved memory: {final_gpu_reserved:.2f} GB")