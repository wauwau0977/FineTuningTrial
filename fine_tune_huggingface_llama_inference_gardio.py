import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel, PeftConfig
import gradio as gr

def run_inference(model_path, question):
    """
    Runs inference on a saved Llama 3 model fine-tuned with LoRA.
    
    Args:
        model_path: Path to the directory containing the fine-tuned model.
        question: A user input string.
    """

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    peft_config = PeftConfig.from_pretrained(model_path)
    base_model = AutoModelForCausalLM.from_pretrained(peft_config.base_model_name_or_path, device_map="auto")
    model = PeftModel.from_pretrained(base_model, model_path, device_map="auto")
    model = model.merge_and_unload()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    model.eval()

    messages = [{"role": "user", "content": question}]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7,
            repetition_penalty=1.2,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id,
        )

    response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    return response

def gradio_inference(question, model_path):
    """
    Gradio interface for the inference function.

    Args:
        question: The question to ask the model.
        model_path: The path to the fine-tuned model.
    """
    try:
        response = run_inference(model_path, question)
        return response
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    lora_finetuned_path = "models/my-llama3-finetuned"  # LoRA fine-tuned model path

    iface = gr.Interface(
        fn=lambda question: gradio_inference(question, lora_finetuned_path),
        inputs=gr.Textbox(lines=2, placeholder="Enter your question here..."),
        outputs=gr.Textbox(lines=5, placeholder="Answer will appear here..."),
        title="Llama 3 LoRA Inference",
        description="Ask a question to the fine-tuned Llama 3 model.",
    )
    iface.launch()