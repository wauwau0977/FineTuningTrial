import time
from gemma3_inference_ollama import GemmaInferenceOllama  # Assuming the previous class is in gemma_inference.py

class GemmaInferenceRunner:
    def __init__(self):
        self.gemma = GemmaInferenceOllama()

    def run(self):
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
            "What are three main states of matter?",
        ]

        for question in questions:
            start_time = time.time()
            answer = self.gemma.inference(question)
            generation_time = time.time() - start_time

            print(f"Q: {question}\n")
            print(f"A: {answer}\n")
            print(f"Generation time: {generation_time:.2f} seconds\n")
            print("-" * 80, "\n")

if __name__ == "__main__":
    runner = GemmaInferenceRunner()
    runner.run()