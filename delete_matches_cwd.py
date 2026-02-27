import os
import sys


def get_files(directory):
    """
    Returns a set of file names (with extension) in the given directory.
    Only includes regular files (not folders).
    """
    try:
        return {
            f
            for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
        }
    except FileNotFoundError:
        print(f"Error: Directory not found -> {directory}")
        sys.exit(1)


def main():
    cwd = os.getcwd()
    other_dir = input("Enter the path of the other directory: ").strip()

    if not os.path.isdir(other_dir):
        print("Invalid directory path.")
        return

    cwd_files = get_files(cwd)
    other_files = get_files(other_dir)

    # Find matching file names (name + extension)
    files_to_delete = cwd_files.intersection(other_files)

    print("\n===== SUMMARY =====")
    print(f"Current Working Directory: {cwd}")
    print(f"Other Directory: {other_dir}")
    print(f"Total files in CWD: {len(cwd_files)}")
    print(f"Total files in Other Directory: {len(other_files)}")
    print(f"Matching files (to be deleted): {len(files_to_delete)}")

    if files_to_delete:
        print("\nFiles that will be deleted:")
        for f in sorted(files_to_delete):
            print(f"  - {f}")

        confirm = input("\nProceed with deletion? (y/n): ").strip().lower()

        if confirm == "y":
            deleted_count = 0
            for file_name in files_to_delete:
                file_path = os.path.join(cwd, file_name)
                try:
                    os.remove(file_path)
                    deleted_count += 1
                except Exception as e:
                    print(f"Failed to delete {file_name}: {e}")

            print(f"\nDeleted {deleted_count} files.")
        else:
            print("Operation cancelled.")
    else:
        print("No matching files found. Nothing to delete.")


if __name__ == "__main__":
    main()
