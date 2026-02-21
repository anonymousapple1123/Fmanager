import os


def rename_files(substring_to_remove):
    current_directory = os.getcwd()
    temp = 1  # debug code
    for filename in os.listdir(current_directory):
        print("Files #", temp, "-> " + filename)  # debug code
        temp += 1  # debug code
        if substring_to_remove in filename:
            new_filename = filename.replace(substring_to_remove, "")

            old_file_path = os.path.join(current_directory, filename)
            new_file_path = os.path.join(current_directory, new_filename)

            os.rename(old_file_path, new_file_path)
            print(f"Renamed: '{filename}' to '{new_filename}'")
