# backup_folder.py

import shutil
import os
import sys

def backup_folder(folder_name):
    if not os.path.exists(folder_name):
        print(f"Error: The folder '{folder_name}' does not exist.")
        sys.exit(1)

    backup_file = f"{folder_name}_backup.zip"

    try:
        print(f"Starting backup of folder: {folder_name}")
        shutil.make_archive(folder_name + "_backup", 'zip', folder_name)
        print(f"Backup completed successfully: {backup_file}")
    except Exception as e:
        print(f"An error occurred during backup: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python backup_folder.py <folder_to_backup>")
        sys.exit(1)

    folder_to_backup = sys.argv[1]
    backup_folder(folder_to_backup)
