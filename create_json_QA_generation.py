import time
import json
from gemma3_inference import GemmaInference

class CreateJsonQA:
    def __init__(self, file_path="learning_json/pretrain_dataset.jsonl"):
        self.file_path = file_path
        self.gemma = GemmaInference()

    def run(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                data = json.loads(line)
                question = data["text"]  # Extract text field as question
                
                start_time = time.time()
                answer = self.gemma.inference(question)
                generation_time = time.time() - start_time

                print(f"Q: {question}\n")
                print(f"A: {answer}\n")
                print(f"Generation time: {generation_time:.2f} seconds\n")
                print("-" * 80, "\n")

if __name__ == "__main__":
    creator = CreateJsonQA()
    creator.run()