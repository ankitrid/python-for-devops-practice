# backup_folder.py

import shutil
import os

# Folder to backup
source_folder = "sample_data"  # Folder you want to back up

# Backup file name
backup_file = "sample_data_backup.zip"

# Create a zip file
shutil.make_archive('sample_data_backup', 'zip', source_folder)

print(f"Backup of '{source_folder}' created as '{backup_file}'")
