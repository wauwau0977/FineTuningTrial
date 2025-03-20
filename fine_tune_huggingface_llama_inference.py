import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel, PeftConfig  # Import PEFT model and config

def run_inference(model_path, questions):
    """
    Runs inference on a saved Llama 3 model fine-tuned with LoRA.
    
    Args:
        model_path: Path to the directory containing the fine-tuned model.
        questions: A list of user input strings.
    """

    # Load the tokenizer.
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    tokenizer.pad_token = tokenizer.eos_token  # Ensure correct padding
    tokenizer.padding_side = "right"  # Ensure consistency

    # Load the PEFT configuration
    peft_config = PeftConfig.from_pretrained(model_path)

    # Load the base model first
    base_model = AutoModelForCausalLM.from_pretrained(peft_config.base_model_name_or_path, device_map="auto")

    # Load the fine-tuned LoRA model
    model = PeftModel.from_pretrained(base_model, model_path, device_map="auto")

    # Merge LoRA into the base model (Improves inference performance)
    model = model.merge_and_unload()

    # Move to GPU if available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
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
                top_k=50,  # Lower values = more deterministic
                top_p=0.95,  # 0.95 keeps diversity while maintaining precision
                temperature=0.7,  # Lower temp for better precision
                repetition_penalty=1.2,  # Reduce repetition
                eos_token_id=tokenizer.eos_token_id,  # Ensure generation stops at EOS
                pad_token_id=tokenizer.eos_token_id,  # Use EOS as pad token
            )

        response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)

        print(f"Question: {question}")
        print(f"Answer: {response}\n\n")

if __name__ == "__main__":
    base_model_path = "NousResearch/Meta-Llama-3.1-8B-Instruct"  # Base model path
    lora_finetuned_path = "models/my-llama3-finetuned"  # LoRA fine-tuned model path

    questions_list = [
        "What is the Warmduscher Project. Explain what it is.",
        "How is the data in Warmduscher Project exactly read from the device and where does it go. Explain in detail!",
        "Explain for Project 'Warmduscher' what the class MeteoSwissService is doing.",
        "Explain for Project 'Warmduscher' what the class MySessionFilter is doing, and what other project classes it does reference.",
        "Explain for Project 'Warmduscher' what the class MyRequestInterceptor is functionally working, and what other project classes it does reference.",
        "Explain for Project 'Warmduscher' what the class HeatingModbusReadService is functionally working, and what other project classes it does reference.",
        "Explain for Project 'Warmduscher' what the class com.x8ing.thsensor.thserver.device.service.impl.HeatingModbusReadService is functionally working, and what other project classes it does reference.",
        "Explain for Project 'Warmduscher' what the class MeteoSwissEntity in package com.x8ing.thsensor.thserver.db.entity.meteoswiss is functionally working, and what other project classes it does reference.",
        "Explain for Project 'Warmduscher' what the class in thclient called boiler-chart.component.ts functionally working, and what other project classes it does reference.",
        "For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/SessionDevice.java' with name 'SessionDevice.java.. Tell me what the class is doing.",
        "What is the capital of France?",
        "What means Kräsemäse in Glattfelderisch?",
        "'Jaudihaudi Jo' in Glattfelden Switzerland what does that mean?",
        "In Glattfelden, Switzerland, what language do they use?",
        "What means the word 'Cheibegruusig' in Glattfelden (Switzerland)?",
        "Was heisst 'Cheibegruusig' in Glattfelderisch?",
        "In Glattfelder-Schweizer-Deutsch what means 'Sausiwegbini Jo'?",
    ]

    run_inference(lora_finetuned_path, questions_list)
