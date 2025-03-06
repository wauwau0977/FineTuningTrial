### Continous Pretraining
axolotl train /workspace/data/FineTuningTrial/axolotl/config1b.yml 
axolotl inference /workspace/data/FineTuningTrial/axolotl/config1b.yml --lora-model-dir="/workspace/data/FineTuningTrial/outputs/llama-8b-finetune" --gradio

