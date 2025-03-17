from unsloth import FastModel
from unsloth.chat_templates import get_chat_template
import time

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


model, tokenizer = FastModel.from_pretrained(
    model_name = "unsloth/gemma-3-27b-it",
    max_seq_length = 2048,  # Adjust as needed
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

    # Time the inference
    start_time = time.time()

    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        temperature=1.0,
        top_p=0.95,
        top_k=64,
    )

    end_time = time.time()

    generation_time = end_time - start_time

    decoded = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    print(f"Q: {question}\n")
    print(f"A: {decoded[0]}\n")
    print(f"Generation time: {generation_time:.2f} seconds\n")
    print("-" * 80, "\n")
