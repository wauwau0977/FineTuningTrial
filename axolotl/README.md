This method is called continued pre-training or domain adaptation.


accelerate launch -m axolotl.cli.train axolotl_config.yaml



axolotl train config.yml


# Reference
tiny-llama/pretrain.yml



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