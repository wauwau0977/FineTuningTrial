import os
import json

# Define the input source directory and output dataset file
SOURCE_DIR = "learning_sources"
OUTPUT_FILE = "finetune_dataset.jsonl"

# Supported file extensions for text-based files
VALID_EXTENSIONS = ('.java', '.ts', '.js', '.html', '.txt', '.xml', '.css', '.json', '.md')

def extract_text_from_files(source_dir, output_file, max_chars_per_sample=4096):
    """
    Reads files from source_dir, extracts text, and writes to a JSONL file for fine-tuning.
    
    Parameters:
      - source_dir (str): Path to the directory containing source code and text files.
      - output_file (str): Path to the output JSONL file.
      - max_chars_per_sample (int): Maximum character length per JSON entry.
    """
    dataset = []
    
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(VALID_EXTENSIONS):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read().strip()
                        if not content:
                            continue

                        # Split into chunks if content is too long
                        for i in range(0, len(content), max_chars_per_sample):
                            chunk = content[i:i + max_chars_per_sample].strip()
                            if chunk:
                                dataset.append({"text": chunk})

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    # Write the dataset to JSONL format
    with open(output_file, "w", encoding="utf-8") as f:
        for entry in dataset:
            json.dump(entry, f)
            f.write("\n")

    print(f"Dataset saved to {output_file} with {len(dataset)} samples.")

# Run the extraction and save the JSONL dataset
extract_text_from_files(SOURCE_DIR, OUTPUT_FILE)
