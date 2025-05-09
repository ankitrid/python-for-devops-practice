# backup_folder.py

import shutil
import os
import sys

# Get folder name from command-line argument
if len(sys.argv) != 2:
    print("Usage: python backup_folder.py <folder_to_backup>")
    sys.exit(1)

source_folder = sys.argv[1]
backup_file = f"{source_folder}_backup.zip"

# Create a zip file
shutil.make_archive(source_folder + "_backup", 'zip', source_folder)

print(f"Backup of '{source_folder}' created as '{backup_file}'")
