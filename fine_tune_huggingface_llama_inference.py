import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def run_inference(model_path, questions):
    """
    Runs inference on a saved Llama 3 model.

    Args:
        model_path: Path to the directory containing the saved model and tokenizer.
        questions: A list of strings, each representing a question.
    """

    # Load the tokenizer.  Important: use AutoTokenizer, *not* a specific tokenizer class.
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    # Ensure pad_token is set (critical for correct batching/padding)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token


    # Load the model
    model = AutoModelForCausalLM.from_pretrained(model_path)

    # Move the model to the GPU if available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)

    # Set the model to evaluation mode
    model.eval()

    for question in questions:
        messages = [{"role": "user", "content": question}]
        prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = tokenizer(prompt, return_tensors="pt").to(device)

        with torch.no_grad():  # Disable gradient calculations
            outputs = model.generate(
                **inputs,
                max_new_tokens=256,
                do_sample=True,
                top_k=10, # 50 some say 0 is better.. lower seems more precise... 
                top_p=0.9, # 0.95 orig
                eos_token_id=tokenizer.eos_token_id,  # Ensure generation stops at EOS
                pad_token_id=tokenizer.eos_token_id,  # Use EOS as pad token (consistent)
            )

        # Decode *only* the generated response (not the prompt)
        response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)

        print(f"Question: {question}")
        print(f"Answer: {response}\n\n")


if __name__ == "__main__":
    model_directory = "models/my-llama3-finetuned"  #  Path to your saved model
    questions_list = [
        "What is the capital of France?",
        "What means Kräsemäse in Glattfelderisch?",
        "'Jaudihaudi Jo' in Glattfelden Switzerland what does that mean?",
        "In Glattfelden, Switzerland, what language do they use?",  # Rephrased
        "What means the word 'Cheibegruusig' in Glattfelden (Switzerland)", # REVERSE LOGIC
        "Was heisst 'Cheibegruusig' in Glattfelderisch?", # REVERSE LOGIC and LANGUAGE SWITCH
        "In Glattfelder-Schweizer-Deutsch what means 'Sausiwegbini Jo'?", # REVERSE
        "In Glattfelder-Schweizer-Deutsch what means 'Sausiwegbini Jo'?", # REVERSE
        "In Glattfelder-Schweizer-Deutsch what means 'Sausiwegbini Jo'?" # REVERSE
    ]
    run_inference(model_directory, questions_list)