import os
import json
import re

# Define the input source directory and output dataset file
SOURCE_DIR = "learning_sources"
OUTPUT_FILE = "learning_json/llm_friendly_dataset.jsonl"
PROJECT_NAME = "Warmduscher"

# Define max token limit (adjust based on your model)
MAX_CHARS_PER_SAMPLE = 2048  

# Supported file extensions
VALID_EXTENSIONS = ('.java', '.ts', '.tsx', '.jsx', '.md', '.txt', '.html')

# Regex patterns for Java and TypeScript function/class/interface detection
FUNC_PATTERN = re.compile(r'^(\s*(public|private|protected|static|async)?\s*\w+\s+\w+\s*\(.*?\)\s*{?)', re.MULTILINE)
CLASS_PATTERN = re.compile(r'^(\s*(class|interface|enum|@Component)\s+\w+)', re.MULTILINE)

def split_code_logically(code, max_chars):
    """
    Splits code into logical blocks based on functions while respecting token limits.
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

        # Start a new chunk when encountering a function definition
        if FUNC_PATTERN.match(line):
            if current_chunk:
                chunks.append("\n".join(current_chunk))
                current_chunk = []
                current_length = 0
        
        # Ensure decorators/annotations are included with the next function
        if i > 0 and lines[i - 1].strip().startswith("@"): 
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

def split_text_logically(content, max_chars):
    """
    Splits markdown, text, or HTML files into max-sized chunks.
    """
    return [content[i:i + max_chars] for i in range(0, len(content), max_chars)]

def extract_text_for_llm_friendly_splitting(source_dir, output_file):
    """
    Reads files from source_dir, extracts text, and writes to a JSONL file in an LLM-friendly way.
    """
    dataset = []

    # Overwrite file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(VALID_EXTENSIONS):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, source_dir)
                
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read().strip()
                        if not content:
                            continue

                        # Determine appropriate splitting strategy
                        if file.lower().endswith(('.md', '.txt', '.html')):
                            chunks = split_text_logically(content, MAX_CHARS_PER_SAMPLE)
                        else:
                            chunks = split_code_logically(content, MAX_CHARS_PER_SAMPLE)

                        # Check for oversized chunks and log them
                        for chunk in chunks:
                            if len(chunk) > MAX_CHARS_PER_SAMPLE:
                                print(f"Warning: Chunk from {file_path} exceeds max token limit, truncating.")
                                chunk = chunk[:MAX_CHARS_PER_SAMPLE]
                            
                            metadata = f"### Project: {PROJECT_NAME}\n" \
                                       f"### File: {file}\n" \
                                       f"### Path: {relative_path}\n\n"

                            dataset.append({"text": metadata + chunk})

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    # Write dataset to JSONL
    with open(output_file, "w", encoding="utf-8") as f:
        for entry in dataset:
            json.dump(entry, f)
            f.write("\n")

    print(f"Dataset saved to {output_file} with {len(dataset)} samples.")

# Run the extraction with LLM-friendly splitting
extract_text_for_llm_friendly_splitting(SOURCE_DIR, OUTPUT_FILE)
