import unsloth
from unsloth import FastModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from unsloth.chat_templates import get_chat_template

model_path = "models/my-gemma-3-finetune"

model, tokenizer = FastModel.from_pretrained(
    model_name = model_path,
    max_seq_length = 2048, # Choose any for long context!
    load_in_4bit = True,  # 4 bit quantization to reduce memory
    load_in_8bit = False, # [NEW!] A bit more accurate, uses 2x memory
    full_finetuning = False, # [NEW!] We have full finetuning now!
    # token = "hf_...", # use one if using gated models
    device_map="auto",         # Automatically place model parts on devices
    max_memory={0: "40GiB", "cpu": "32GiB"},  # Limit memory per device
    offload_folder="offload",   # Offload model weights to disk if needed
     local_files_only=True, # Ensure loading from local files
     ignore_mismatched_sizes=True  # HACK!!! TODO Ignore any weights that don’t match
    # not helping! attn_implementation='eager'  # TODO: Actually not so sure if good or not... at least it warns if not set!!! https://github.com/unslothai/unsloth/issues/2025
)

print("Local model loaded with success")

#tokenizer = AutoTokenizer.from_pretrained(model_path)
#model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")

#tokenizer = get_chat_template(tokenizer, chat_template="gemma-3")

question = "What is the capital of France?"
messages = [{"role": "user", "content": question}]
text = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)

print("Text tokinized")


outputs = model.generate(
    **inputs,
    max_new_tokens=128,
    temperature=1.0,
    top_p=0.95,
    top_k=64,
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)