from unsloth import FastModel
from unsloth.chat_templates import get_chat_template
import torch
import time

class GemmaInference:
    def __init__(self, model_name="unsloth/gemma-3-27b-it", max_seq_length=4096):
        self.model_name = model_name
        self.max_seq_length = max_seq_length
        self.load_model()

    def load_model(self):
        self.model, self.tokenizer = FastModel.from_pretrained(
            model_name=self.model_name,
            max_seq_length=self.max_seq_length,
            load_in_4bit=True,
        )
        self.tokenizer = get_chat_template(
            self.tokenizer,
            chat_template="gemma-3",
        )

    def inference(self, question, max_new_tokens=512, temperature=1.0, top_p=0.95, top_k=64):
        messages = [{
            "role": "user",
            "content": [{"type": "text", "text": question}]
        }]

        text = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
        )

        inputs = self.tokenizer([text], return_tensors="pt").to("cuda")
        input_len = inputs.input_ids.shape[1]

        try:
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
            )
            decoded = self.tokenizer.batch_decode(outputs[:, input_len:], skip_special_tokens=True)
            return decoded[0].strip()
        except torch.cuda.OutOfMemoryError as e:
            print(f"CUDA OOM error! Skipping question: {question}\nError details: {str(e)}")
            torch.cuda.empty_cache()
            return None