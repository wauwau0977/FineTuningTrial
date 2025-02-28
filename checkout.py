import os
import json
import subprocess

# Step 1: Clone the Warmduscher repository (if not already cloned)
repo_url = "https://github.com/wauwau0977/Warmduscher.git"
repo_dir = "Warmduscher"

if not os.path.exists(repo_dir):
    subprocess.run(["git", "clone", repo_url])
    print(f"Cloned {repo_url} into {repo_dir}")
else:
    print(f"Repository {repo_dir} already exists.")