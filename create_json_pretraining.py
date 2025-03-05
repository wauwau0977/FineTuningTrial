import os
import json
import re

# Define input/output directories
SOURCE_DIR = "learning_sources"
OUTPUT_DIR = "learning_json"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "pretrain_dataset.jsonl")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Token/character limits
MAX_CHARS_PER_SAMPLE = 4000  # Adjust based on model context size
VALID_EXTENSIONS = ('.java', '.ts', '.tsx', '.jsx')

# Regex patterns for class and function/method detection (better logical splits)
CLASS_PATTERN = re.compile(r'^\s*(class|interface|enum|@Component)\s+\w+', re.MULTILINE)
FUNCTION_PATTERN = re.compile(r'^\s*(public|private|protected|static|\s)*\s+[\w<>\[\]]+\s+\w+\s*\(.*\)\s*{', re.MULTILINE)

def clean_code(code):
    """Removes unnecessary empty lines and trims whitespace."""
    return "\n".join([line.rstrip() for line in code.split("\n") if line.strip()])

def split_code_into_chunks(code, max_chars):
    """
    Splits code logically by function/method or class boundaries while respecting token limits.
    """
    chunks = []
    current_chunk = []
    current_length = 0
    lines = code.split("\n")

    for i, line in enumerate(lines):
        line_length = len(line) + 1  # Account for newline

        # If adding this line exceeds the limit, save the chunk
        if current_length + line_length > max_chars and current_chunk:
            chunks.append("\n".join(current_chunk))
            current_chunk = []
            current_length = 0

        # Start a new chunk when encountering a class or function declaration
        if CLASS_PATTERN.match(line) or FUNCTION_PATTERN.match(line):
            if current_chunk:
                chunks.append("\n".join(current_chunk))
                current_chunk = []
                current_length = 0

        current_chunk.append(line)
        current_length += line_length

    # Add any remaining code as a final chunk
    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks

def extract_code_for_pretraining(source_dir, output_file):
    """
    Reads files from source_dir, extracts code, and writes to a JSONL file suitable for pretraining.
    """
    dataset = []

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Overwrite file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(VALID_EXTENSIONS):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read().strip()
                        if not content:
                            continue

                        # Clean and split the code into logical chunks
                        content = clean_code(content)
                        chunks = split_code_into_chunks(content, MAX_CHARS_PER_SAMPLE)

                        # Add each chunk as a standalone pretraining sample
                        for chunk in chunks:
                            dataset.append({"text": chunk})

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    # Write dataset to JSONL
    with open(output_file, "w", encoding="utf-8") as f:
        for entry in dataset:
            json.dump(entry, f)
            f.write("\n")

    print(f"Pretraining dataset saved to {output_file} with {len(dataset)} samples.")

# Run dataset extraction for pretraining
extract_code_for_pretraining(SOURCE_DIR, OUTPUT_FILE)
