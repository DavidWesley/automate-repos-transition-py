import os
import subprocess

from prints import print_err, print_warning, print_debug


def list_files(folder_path: str):
	print_debug(f"list_files: {folder_path}")
	if os.path.exists(folder_path) is False:
		return None

	filenames = list(
		set([
			os.path.splitext(file) for file in os.listdir(folder_path)
			if os.path.isfile(os.path.join(folder_path, file))
		]))

	return filenames


def format_files(folder_path: str) -> bool:
	print_debug(f"format_files: {folder_path}")

	try:
		subprocess.run('npm run lint:all', shell=True, check=True)
	except:
		print_warning(f"Could not lint the files in '{folder_path}'")
		return False

	return True


def move_file(filepath: str, path_destination: str) -> None:
	print_debug(f"move_file: {filepath} {path_destination}")

	if os.path.exists(filepath) is False:
		print_err(f"Invalid path: '{filepath}'")
		return
	if os.path.isfile(filepath) is False:
		print_err(f"Invalid file: '{filepath}'")
		return

	try:
		subprocess.run(["mv", filepath, path_destination])
	except:
		print_warning(f"Could not move file '{filepath}' to '{path_destination}'")


def copy_file(filepath: str, folder_destination: str) -> None:
	print_debug(f"copy_file: {filepath} {folder_destination}")

	if os.path.exists(filepath) is False:
		print_err(f"Invalid path: '{filepath}'")
		return
	if os.path.isfile(filepath) is False:
		print_err(f"Invalid file: '{filepath}'")
		return
	if os.path.isdir(folder_destination) is False:
		print_err(f"Invalid folder: '{folder_destination}'")
		return

	try:
		subprocess.run(["cp", filepath, folder_destination])
	except:
		print_warning(f"Could not copy file '{filepath}' to '{folder_destination}'")


def commit_file(filepath: str, message: str) -> None:
	print_debug(f"commit_file: {filepath} {message}")

	if os.path.exists(filepath) is False:
		print_err(f"Invalid path: '{filepath}'")
		return
	if os.path.isfile(filepath) is False:
		print_err(f"Invalid file: '{filepath}'")
		return

	try:
		subprocess.run('git reset', shell=True)
		subprocess.run(['git', 'add', filepath])
		subprocess.run(['git', 'commit', '-m', message, "--no-verify"])
	except:
		print_warning(f"Could not commit the file '{filepath}' with the message '{message}'")
