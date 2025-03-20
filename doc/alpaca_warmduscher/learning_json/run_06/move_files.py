import os
import shutil
import re

def organize_files(directory):
    """
    Organizes files in the given directory into subfolders based on their group.

    Args:
        directory (str): The path to the directory containing the files.
    """

    files = sorted(os.listdir(directory))
    group_counter = 1
    current_group = None
    group_files = []

    for filename in files:
        if not filename.endswith(".md"): # skip if not md file
            continue

        match = re.match(r"(\d+)_.*", filename)
        if match:
            group_id = match.group(1)
            if current_group is None:
                current_group = group_id
            if group_id == current_group:
                group_files.append(filename)
            else:
                # Create subfolder and move files
                subfolder_name = f"Q_{str(group_counter).zfill(3)}"
                subfolder_path = os.path.join(directory, subfolder_name)
                os.makedirs(subfolder_path, exist_ok=True)

                for file_to_move in group_files:
                    source_path = os.path.join(directory, file_to_move)
                    destination_path = os.path.join(subfolder_path, file_to_move)
                    shutil.move(source_path, destination_path)

                # Reset for the next group
                group_counter += 1
                current_group = group_id
                group_files = [filename]
        else:
            print(f"Warning: Filename '{filename}' does not match expected pattern.")
            # Do not stop processing, continue with next file
            continue

    # Move the last group of files
    if group_files:
        subfolder_name = f"Q_{str(group_counter).zfill(3)}"
        subfolder_path = os.path.join(directory, subfolder_name)
        os.makedirs(subfolder_path, exist_ok=True)

        for file_to_move in group_files:
            source_path = os.path.join(directory, file_to_move)
            destination_path = os.path.join(subfolder_path, file_to_move)
            shutil.move(source_path, destination_path)

if __name__ == "__main__":
    directory_path = "."  # Replace with your directory path if needed
    organize_files(directory_path)
    print("Files organized into subfolders.")