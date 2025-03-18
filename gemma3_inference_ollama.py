import ollama

class GemmaInferenceOllama:
    def __init__(self, model_name="gemma3:27b", max_seq_length=8000):
        self.model_name = model_name
        self.max_seq_length = max_seq_length

    def inference(self, question, temperature=1.0, top_p=0.95, top_k=64):
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": question,
                    }
                ],
                options={
                    "temperature": temperature,
                    "top_p": top_p,
                    "top_k": top_k,
                    "num_ctx": self.max_seq_length,
                },
            )
            return response['message']['content'].strip()
        except Exception as e:
            print(f"Error during inference: {e}")
            return None
