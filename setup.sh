#!/bin/bash

python3 -m venv finetune_env
source finetune_env/bin/activate  
pip install -r requirements.txt


mkdir learning_sources
cd learning_sources
git clone https://github.com/wauwau0977/Warmduscher.git

python3 create_json.py

git config --global user.name "wauwau0977"
git config --global user.email "patrick.heusser@gmail.com"

echo "dev" > ~/.gitcommittemplate
git config --global commit.template ~/.gitcommittemplate



# start jupyter notbook if not yet running
pgrep -f "jupyter-notebook" > /dev/null || nohup jupyter notebook > jupyter.log 2>&1 &


# login hugging face
huggingface-cli login

echo -e "run now"
echo -e "source finetune_env/bin/activate "

