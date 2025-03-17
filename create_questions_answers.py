import torch
from transformers import AutoTokenizer, Gemma3ForCausalLM

ckpt = "google/gemma-3-27b-it"

# Define the device map and memory allocation
device_map = {
    "transformer.wte": 0,
    "transformer.h": 0,
    "transformer.ln_f": 0,
    "lm_head": 0,
}
max_memory = {
    0: "40GiB",  # Allocate 40 GiB to GPU 0
    "cpu": "48GiB"  # Allocate 48 GiB to CPU RAM
}

# Load the model with the specified device map and memory allocation
model = Gemma3ForCausalLM.from_pretrained(
    ckpt,
    torch_dtype=torch.bfloat16,
    device_map=device_map,
    max_memory=max_memory
)

tokenizer = AutoTokenizer.from_pretrained(ckpt)

messages = [
    {
        "role": "system",
        "content": [{"type": "text", "text": "You are a helpful assistant who is fluent in Shakespearean English"}]
    },
    {
        "role": "user",
        "content": [{"type": "text", "text": "Who are you?"}]
    },
]

inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=True,
    return_dict=True, return_tensors="pt"
).to(model.device)

input_len = inputs["input_ids"].shape[-1]

generation = model.generate(**inputs, max_new_tokens=100, do_sample=False)
generation = generation[0][input_len:]

decoded = tokenizer.decode(generation, skip_special_tokens=True)
print(decoded)
