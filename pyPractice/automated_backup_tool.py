import os
import shutil
from datetime import datetime

def list_files(directory):
	return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def copy_file(source, destination):
	shutil.copy2(source, destination)

def create_backup_directory(base_backup_dir):
	timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	backup_dir = os.path.join(base_backup_dir, f"backup_{timestamp}")
	os.makedirs(backup_dir, exist_ok=True)
	return backup_dir

def backup_files(source_dir, backup_dir):
	files = list_files(source_dir)
	for file in files:
		source_path = os.path.join(source_dir, file)
		destination_path = os.path.join(backup_dir, file)
		copy_file(source_path, destination_path)
		print(f"Backed up: {file}")

def write_log(backup_dir, log_file, files):
	with open(log_file, "a") as log:
		log.write(f"Backup created: {backup_dir}\n")
		for file in files:
			log.write(f" -{file}")
		log.write("\n")

def main():
	print("Automated Backup Tool")
	source_dir = input("Enter the source directory to backup: ")
	backup_base_dir = input("Enter the base directory for backups: ")
	log_file = input("Enter the log file path: ")
	if not os.path.exists(source_dir):
		print("Source directory does not exist. Exiting.")
		return
	
	os.makedirs(backup_base_dir, exist_ok=True)
	backup_dir = create_backup_directory(backup_base_dir)
	files = backup_files(source_dir, backup_dir)
	write_log(backup_dir, log_file, files)

	print(f"Backup completed successfully. Log saved to: {log_file}")

if __name__ == "__main__":
	main()