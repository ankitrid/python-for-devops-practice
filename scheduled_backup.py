# scheduled_backup.py

import shutil
import os
import time
from datetime import datetime

def backup_folder(folder_name):
    if not os.path.exists(folder_name):
        print(f"Error: The folder '{folder_name}' does not exist.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{folder_name}_backup_{timestamp}.zip"

    try:
        print(f"[{datetime.now()}] Starting backup of folder: {folder_name}")
        shutil.make_archive(folder_name + "_backup_" + timestamp, 'zip', folder_name)
        print(f"[{datetime.now()}] Backup completed: {backup_file}\n")
    except Exception as e:
        print(f"An error occurred during backup: {e}")

if __name__ == "__main__":
    folder_to_backup = "sample_data"  # you can change this
    while True:
        backup_folder(folder_to_backup)
        time.sleep(60)  # Wait 60 seconds before next backup
