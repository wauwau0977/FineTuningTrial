from unsloth import FastModel
from unsloth.chat_templates import get_chat_template


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
    model_name = "unsloth/gemma-3-4b-it",
    max_seq_length = 2048,  # Adjust as needed
    load_in_4bit = True,  # 4-bit quantization for lower memory usage
)

tokenizer = get_chat_template(
    tokenizer,
    chat_template = "gemma-3",
)

messages = [{
    "role": "user",
    "content": [{
        "type": "text",
        "text": "Continue the sequence: 1, 1, 2, 3, 5, 8,",
    }]
}]

text = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
)

inputs = tokenizer([text], return_tensors="pt").to("cuda")

outputs = model.generate(
    **inputs,
    max_new_tokens=64,
    temperature=1.0,
    top_p=0.95,
    top_k=64,
)

decoded = tokenizer.batch_decode(outputs, skip_special_tokens=True)
print(decoded[0])