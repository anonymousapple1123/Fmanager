import shutil
from pathlib import Path


def sync_folders(source_dir, dest_dir, extensions):
    # Convert strings to Path objects
    source = Path(source_dir)
    destination = Path(dest_dir)

    # Ensure destination exists
    if not destination.exists():
        print(f"Creating destination: {destination}")
        destination.mkdir(parents=True)

    print(f"Syncing files from {source} to {destination}...")

    # Iterate through files in source
    for file_path in source.iterdir():
        # Check if it's a file and has the right extension
        if file_path.is_file() and file_path.suffix.lower() in extensions:
            dest_file = destination / file_path.name

            # Sync logic: Copy if file doesn't exist OR source is newer
            if (
                not dest_file.exists()
                or file_path.stat().st_mtime > dest_file.stat().st_mtime
            ):
                print(f"Copying: {file_path.name}")
                shutil.copy2(
                    file_path, dest_file
                )  # copy2 preserves metadata (timestamps)
            else:
                pass  # File is already up to date

    print("Sync complete!")


if __name__ == "__main__":
    # CONFIGURATION
    # Current working directory
    SRC = Path.cwd()

    # Replace this with your actual mounted drive path
    # Example: "/Volumes/USB_DRIVE/Books" or "E:/Books"
    DEST = "/Volumes/H/Fmanager/"

    # File types to include
    EXTS = {".pdf", ".txt", ".epub", ".mobi", ".docx"}

    sync_folders(SRC, DEST, EXTS)
