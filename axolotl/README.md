This method is called continued pre-training or domain adaptation.


accelerate launch -m axolotl.cli.train axolotl_config.yaml


### Continous Pretraining
axolotl train /workspace/data/FineTuningTrial/axolotl/config1b.yml 
axolotl inference /workspace/data/FineTuningTrial/axolotl/config1b.yml --lora-model-dir="/workspace/data/FineTuningTrial/outputs/llama-8b-finetune" --gradio

````
<|im_start|>system
You are Tamer, a strange IT nerd<|im_end|>
<|im_start|>user
Hello, who are you?<|im_end|>
<|im_start|>assistant
````

````
<|im_start|>system
You are an IT expert of Warmduscher, that's an IT app with the main packages being com.x8ing.thsensor.thserver.<|im_end|>
<|im_start|>user
How does the main class work?<|im_end|>
<|im_start|>assistant
````

# axolotl train /workspace/FineTuningTrial/axolotl/config2.yml



axolotl inference /workspace/FineTuningTrial/axolotl/config2.yml --lora-model-dir="./outputs/model-out-my-01-tiny-llama-1B-v2" --gradio


# Llama 3-70B
axolotl train /workspace/data/FineTuningTrial/axolotl/config3.yml
axolotl inference /workspace/data/FineTuningTrial/axolotl/config3.yml --lora-model-dir="/workspace/data/FineTuningTrial/outputs/out/qlora-llama3-70b" --gradio

````
### Instruction:
List all the capitals of Europe.  Give a quick explanation of each city and it's population. 

### Response:
````

````
### Instruction:
Make a nice java class to pull the weather data from Weather underground using spring boot. Use lombook for the beans in java. 

### Response:
````

# Starcoder2 3B
axolotl train /workspace/data/FineTuningTrial/axolotl/config4.yml

# Reference
tiny-llama/pretrain.yml


# Promting
<|system|>
You are a java programmer for the warmduscher app</s>
<|user|>
Write a java class for ThserverApplication </s>
<|assistant|>



What Happens Under the Hood?
The model already has general knowledge (from original LLaMA training).
It learns additional patterns from the new dataset (e.g., Java, TypeScript, financial data, etc.).
The result is a domain-adapted version of LLaMA (e.g., a code-specific LLaMA).
🚀 Final Takeaways
✅ You can fine-tune LLaMA with pre-training-style data (raw "text").
✅ This method is called continued pre-training or domain adaptation.
✅ Axolotl supports "text"-only format for additional knowledge training.
✅ The final model remembers LLaMA's original training but becomes more specialized.

Would you like a script to evaluate the trained model after continued pre-training? 🚀