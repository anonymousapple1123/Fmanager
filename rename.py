import os


def rename_files(substring_to_remove):
    current_directory = os.getcwd()

    for filename in os.listdir(current_directory):
        # Check if the substring exists in the file name
        if substring_to_remove in filename:
            # Create a new filename by replacing the substring with an empty string
            new_filename = filename.replace(substring_to_remove, "")

            # Construct full file path
            old_file_path = os.path.join(current_directory, filename)
            new_file_path = os.path.join(current_directory, new_filename)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: '{filename}' to '{new_filename}'")


if __name__ == "__main__":
    # Specify the substring to remove
    substring = "snippet"
    rename_files(substring)
