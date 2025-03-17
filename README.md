# FineTuningTrial

git clone https://wauwau0977:YOUR_PERSONAL_ACCESS_TOKEN@github.com/wauwau0977/FineTuningTrial.git
run setup.sh

# use token to login
huggingface-cli login

source finetune_env/bin/activate  
python3 create_json_pretraining.py 
python3 create_questions_answers_unsloth.py

# useful commands:
nvidia-smi


# tmux
in file: ~/.tmux.conf add
set -g mouse on
run: tmux source-file ~/.tmux.conf

# Gemma 3
spec: https://ai.google.dev/gemma/docs/core