import logging
import os

logger = logging.getLogger()


def rename_files(substring_to_remove):
    files_renamed = 0
    total_files = 0
    current_directory = os.getcwd()
    for filename in os.listdir(current_directory):
        total_files += 1
        if substring_to_remove in filename:
            try:
                new_filename = filename.replace(substring_to_remove, "")

                old_file_path = os.path.join(current_directory, filename)
                new_file_path = os.path.join(current_directory, new_filename)
            except Exception as e:
                logger.exception("Error in renaming<os.path.join>[", filename, "]")
                raise
            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: '{filename}' to '{new_filename}'")
                files_renamed += 1
            except Exception as e:
                logger.exception("Error in renaming<os.rename>[", filename, "]")
                raise
    print(
        "rename.py [ Total Files: ", total_files, " Files Renamed: ", files_renamed, "]"
    )
