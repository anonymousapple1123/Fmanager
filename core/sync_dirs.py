import shutil
import sys
from pathlib import Path

ALLOWED_EXTENSIONS = {".pdf", ".txt", ".epub", ".mobi", ".docx"}


def get_eligible_files(directory: Path):
    """Return dictionary {filename: Path} for allowed files."""
    return {
        f.name: f
        for f in directory.iterdir()
        if f.is_file() and f.suffix.lower() in ALLOWED_EXTENSIONS
    }


def validate_directory(path_str):
    path = Path(path_str)
    if not path.exists() or not path.is_dir():
        print(f"❌ Invalid directory: {path}")
        sys.exit(1)
    return path


def two_way_sync(dir1, dir2):
    dir1 = validate_directory(dir1)
    dir2 = validate_directory(dir2)

    print("\nScanning directories...")

    dir1_all = [f for f in dir1.iterdir() if f.is_file()]
    dir2_all = [f for f in dir2.iterdir() if f.is_file()]

    dir1_files = get_eligible_files(dir1)
    dir2_files = get_eligible_files(dir2)

    to_copy_1_to_2 = []
    to_copy_2_to_1 = []

    all_filenames = set(dir1_files.keys()).union(dir2_files.keys())

    for name in all_filenames:
        file1 = dir1_files.get(name)
        file2 = dir2_files.get(name)

        if file1 and not file2:
            to_copy_1_to_2.append(name)

        elif file2 and not file1:
            to_copy_2_to_1.append(name)

        elif file1 and file2:
            # Compare modification times
            if file1.stat().st_mtime > file2.stat().st_mtime:
                to_copy_1_to_2.append(name)
            elif file2.stat().st_mtime > file1.stat().st_mtime:
                to_copy_2_to_1.append(name)
            # if equal → do nothing

    # ===== SUMMARY =====
    print("\n========== TWO-WAY SYNC SUMMARY ==========")
    print(f"Folder 1: {dir1}")
    print(f"Folder 2: {dir2}")
    print(f"Total files in Folder 1: {len(dir1_all)}")
    print(f"Total files in Folder 2: {len(dir2_all)}")
    print(f"Eligible files in Folder 1: {len(dir1_files)}")
    print(f"Eligible files in Folder 2: {len(dir2_files)}")
    print(f"\nFiles to copy Folder1 ➜ Folder2: {len(to_copy_1_to_2)}")
    print(f"Files to copy Folder2 ➜ Folder1: {len(to_copy_2_to_1)}")
    print("Allowed extensions:", ", ".join(sorted(ALLOWED_EXTENSIONS)))
    print("==========================================")

    if not to_copy_1_to_2 and not to_copy_2_to_1:
        print("\n Both folders are already in sync.")
        return

    confirm = input("\nProceed with two-way sync? (y/n): ").strip().lower()
    if confirm != "y":
        print("❌ Sync cancelled.")
        return

    copied_count = 0

    # Copy dir1 → dir2
    for name in to_copy_1_to_2:
        try:
            print(f" {name}  (Folder1 ➜ Folder2)")
            shutil.copy2(dir1 / name, dir2 / name)
            copied_count += 1
        except Exception as e:
            print(f"[ ERROR ]: Failed copying {name}: {e}")

    # Copy dir2 → dir1
    for name in to_copy_2_to_1:
        try:
            print(f"{name}  (Folder2 ➜ Folder1)")
            shutil.copy2(dir2 / name, dir1 / name)
            copied_count += 1
        except Exception as e:
            print(f"⚠️ Failed copying {name}: {e}")

    print(f"\nTwo-way sync complete! {copied_count} file(s) synced.")


def initiate_sync():
    print("SMART TWO-WAY SYNC")
    folder1 = input("Enter first folder path (default = current directory): ").strip()
    folder2 = input("Enter second folder path: ").strip()

    if not folder1:
        folder1 = Path.cwd()

    two_way_sync(folder1, folder2)
