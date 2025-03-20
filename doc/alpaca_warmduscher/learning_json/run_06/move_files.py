import os
import shutil
import re
import sys

def organize_files(directory):
    """
    Organizes markdown files in the given directory into subfolders based on conversation groups.

    A new group starts when a file name ends with '_instruction_Q0.md'. All subsequent markdown
    files are added to that group until the next file that matches the Q0 pattern is encountered.
    Each group is moved into a subfolder named incrementally as Q_XXX (e.g., Q_001, Q_002, etc.).
    
    Files that do not belong to any group (e.g., a file before the first Q0 marker) are skipped.
    """
    print(f"Organizing files in: {directory}")
    try:
        files = sorted(os.listdir(directory))
    except Exception as e:
        print(f"Error listing directory {directory}: {e}")
        return

    print(f"Found files: {files}")
    group_counter = 1
    current_group = []  # List to collect files for the current group

    for filename in files:
        if not filename.endswith(".md"):
            print(f"Skipping non-md file: {filename}")
            continue

        # Check if this file marks the start of a new group.
        if re.search(r"_instruction_Q0\.md$", filename):
            print(f"Found new group marker in file: {filename}")
            # If a group is already in progress, move it to its subfolder.
            if current_group:
                subfolder_name = f"Q_{group_counter:03d}"
                subfolder_path = os.path.join(directory, subfolder_name)
                os.makedirs(subfolder_path, exist_ok=True)
                print(f"Moving group {group_counter} files: {current_group} to folder {subfolder_path}")
                for f in current_group:
                    src = os.path.join(directory, f)
                    dst = os.path.join(subfolder_path, f)
                    shutil.move(src, dst)
                group_counter += 1
                current_group = []
            # Start a new group with this file.
            current_group.append(filename)
        else:
            # If a group has started, add this file to the current group.
            if current_group:
                current_group.append(filename)
            else:
                print(f"Skipping '{filename}' since no group has started (no Q0 encountered yet).")
    
    # After iterating, move any remaining files in the last group.
    if current_group:
        subfolder_name = f"Q_{group_counter:03d}"
        subfolder_path = os.path.join(directory, subfolder_name)
        os.makedirs(subfolder_path, exist_ok=True)
        print(f"Moving final group {group_counter} files: {current_group} to folder {subfolder_path}")
        for f in current_group:
            src = os.path.join(directory, f)
            dst = os.path.join(subfolder_path, f)
            shutil.move(src, dst)

if __name__ == "__main__":
    # Get the target directory from the command-line argument.
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
    else:
        directory_path = "."
    organize_files(directory_path)
    print("Files organized into subfolders.")
