import os
import json
import re

# Define the input source directory and output dataset file
SOURCE_DIR = "learning_sources"
OUTPUT_DIR = "learning_json"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "llm_friendly_dataset.jsonl")
PROJECT_NAME = "Warmduscher"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define max token limit (adjust based on your model)
MAX_CHARS_PER_SAMPLE = 12000  

# Supported file extensions
VALID_EXTENSIONS = ('.java', '.ts', '.tsx', '.jsx')

# Regex patterns for Java and TypeScript class detection
CLASS_PATTERN = re.compile(r'^\s*(class|interface|enum|@Component)\s+\w+', re.MULTILINE)

def split_code_logically(code, max_chars):
    """
    Splits code into logical blocks while respecting token limits.
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

        # Start a new chunk when encountering a class declaration
        if CLASS_PATTERN.match(line):
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

def extract_code_for_alpaca(source_dir, output_file):
    """
    Reads files from source_dir, extracts code, and writes to an Alpaca-style JSONL file.
    """
    dataset = []

    # Ensure the output directory exists before writing
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Overwrite file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(VALID_EXTENSIONS):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, source_dir)  # Extract relative path

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read().strip()
                        if not content:
                            continue

                        # Split code logically
                        chunks = split_code_logically(content, MAX_CHARS_PER_SAMPLE)

                        # Convert each chunk to Alpaca format
                        for chunk in chunks:
                            if len(chunk) > MAX_CHARS_PER_SAMPLE:
                                print(f"Warning: Chunk from {file_path} exceeds max token limit, truncating.")
                                chunk = chunk[:MAX_CHARS_PER_SAMPLE]

                            dataset.append({
                                "instruction": f"You work for a project called {PROJECT_NAME}. Your task is to write source code for {relative_path}. Directly output the source content.",
                                "input": "",
                                "output": chunk
                            })

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    # Write dataset to JSONL
    with open(output_file, "w", encoding="utf-8") as f:
        for entry in dataset:
            json.dump(entry, f)
            f.write("\n")

    print(f"Dataset saved to {output_file} with {len(dataset)} samples.")

# Run the extraction for Alpaca-style dataset
extract_code_for_alpaca(SOURCE_DIR, OUTPUT_FILE)
