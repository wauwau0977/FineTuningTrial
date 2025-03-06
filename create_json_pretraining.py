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
MAX_CHARS_PER_SAMPLE = 8000  # Adjust based on model context size

VALID_EXTENSIONS = (
    # Programming Languages
    '.java', '.ts', '.tsx', '.jsx', '.js', '.py', '.cpp', '.c', '.cc', '.cxx', '.h', '.hpp', '.cs',
    '.go', '.rb', '.php', '.swift', '.kt', '.rs', '.pl', '.r', '.scala', '.m', '.sh', '.bash', 
    '.ps1', '.lua', '.m', '.hs', '.erl', '.ex', '.exs', '.dart', '.coffee', '.vhdl', '.vhd', 
    '.v', '.vh', '.adb', '.ads', '.f', '.f90', '.f95', '.pas', '.cob', '.cbl', '.asm', '.s', 
    '.jl', '.clj', '.cljs', '.fs', '.fsi', '.fsx', '.ml', '.mli', '.groovy', '.tcl', '.scm', 
    '.ss', '.pl', '.pro', '.lisp', '.lsp', '.rkt', '.sas', '.sps', '.do', '.ado', '.awk', 
    '.make', '.mk', '.bat', '.cmd',

    # Markup and Data Languages
    '.html', '.htm', '.xml', '.yaml', '.yml', '.json', '.md', '.tex', '.toml', '.ini', 
    '.rdf', '.sgml', '.sgm', '.csv',

    # Stylesheet Languages
    '.css', '.sass', '.scss', '.less', '.styl',

    # Database and Config Files
    '.sql', '.sqlite', '.db', '.properties', '.config', '.env',

    # Template and Miscellaneous Files
    '.hbs', '.ejs', '.jinja', '.jinja2', '.mustache', '.log', '.txt'
)

PROJECT_NAME = "Warmduscher"  # Change this to your actual project name

def clean_code(code):
    """Removes unnecessary empty lines and trims whitespace."""
    return "\n".join([line.rstrip() for line in code.split("\n") if line.strip()])

def split_code_if_needed(code, max_chars):
    """
    Only split the code if it exceeds max_chars, otherwise return a single entry.
    """
    if len(code) <= max_chars:
        return [code]  # Return as a single chunk if it fits

    # Otherwise, split the code into chunks based on line breaks
    chunks = []
    current_chunk = []
    current_length = 0
    lines = code.split("\n")

    for line in lines:
        line_length = len(line) + 1  # Account for newline

        # If adding this line exceeds the limit, save the chunk
        if current_length + line_length > max_chars and current_chunk:
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
    Reads files from source_dir, extracts code, and writes to a JSONL file for pretraining.
    Embeds metadata directly into the "text" field.
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
                relative_path = os.path.relpath(file_path, source_dir)  # Get relative path

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read().strip()
                        if not content:
                            continue

                        # Clean the code
                        content = clean_code(content)
                        chunks = split_code_if_needed(content, MAX_CHARS_PER_SAMPLE)

                        # Add each chunk as a pretraining sample with metadata in text format
                        for chunk in chunks:
                            dataset.append({
                                "text": f"project: {PROJECT_NAME}\nfilename: {file}\npath: {relative_path}\n\n{chunk}"
                            })

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
