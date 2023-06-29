import os
import sys
import re

import requests
from bs4 import BeautifulSoup

import subcommands
from prints import print_err, print_info, print_header, print_warning

FOLDERS_NAMES = [
	'structures',
	'maths',
	'adhoc',
	'beginner',
	'graphs',
	'strings',
	'geometry',
	'paradigms',
	'SQL'
]

VALID_FILE_EXTENSIONS = [".js", ".sql"]


def main():
	if len(sys.argv) != 3:
		print_err("Incorrect number of arguments!")
		return
	elif os.path.isdir(sys.argv[1]) is False:
		print_err("The first argument is not a valid directory path")
	elif os.path.isdir(sys.argv[2]) is False:
		print_err("The second argument is not a valid directory path")
		return

	path_from, path_to = sys.argv[1:3]

	print_header(f"Transferring files from '{path_from}' to '{path_to}'", end="\n\n")
	for folder_name in FOLDERS_NAMES:
		folder_path_to = os.path.abspath(os.path.join(path_to, folder_name))
		folder_path_from = os.path.abspath(os.path.join(path_from, folder_name))

		if os.path.exists(folder_path_to) is False:
			os.mkdir(os.path.join(path_to, folder_name))
			print_info(f"Create '{folder_name}' in '{path_to}' directory")

		files = subcommands.list_files(folder_path_from)

		if files is None:
			continue

		print_info(f"Copying files from '{folder_path_from}' to '{folder_path_to}'...")
		for (file_name, file_extension) in files:
			if file_extension in VALID_FILE_EXTENSIONS:
				original_file_name = f"{file_name}{file_extension}"
				modified_file_name = f"{file_name.split('.')[0]}{file_extension}"
				file_path_from = os.path.join(folder_path_from, original_file_name)
				file_path_to = os.path.join(folder_path_to, modified_file_name)

				subcommands.copy_file(file_path_from, folder_path_to)

				if file_name.find('.') != -1:
					subcommands.move_file(os.path.join(folder_path_to, original_file_name), file_path_to)

		print_info(f"Formatting file before commit then...")
		if subcommands.format_files(folder_path_to) is False:
			continue

		print_info(f"Committing files from '{folder_path_from}' to '{folder_path_to}'...")
		for (file_name, file_extension) in subcommands.list_files(folder_path_to):
			file_path = os.path.join(folder_path_to, f"{file_name}{file_extension}")
			problem_url = generate_url_from_problem_name(file_name)
			title = get_html_file_title_from_url(problem_url)

			if title is not None:
				subcommands.commit_file(file_path, f"feat: {normalize_title(title)}")


def get_html_file_title_from_url(url: str):
	try:
		req = requests.get(url)
		if req.status_code == 404:
			print_warning("Making default request")
			url = url.replace("_en", "")
			req = requests.get(url)

		if req.ok:
			html = requests.get(url).content.decode()
			soup = BeautifulSoup(html, 'html.parser')
			if soup.title is not None:
				return soup.title.text
	except:
		print_warning(f"It appears that the path '{url}' is not valid")
		return None


def generate_url_from_problem_name(name: int | str) -> str:
	template_url = 'https://www.beecrowd.com.br/repository/UOJ_????_en.html'
	result_url = template_url.replace("????", str(name))
	return result_url


def normalize_title(title: str) -> str:
	pattern = r'(\d{4})(\s+?\d{4}\s+?)?( ?- ?)?(.*)$'
	striped = ' '.join(title.split()).removeprefix("bee").strip()
	match = re.search(pattern, striped)

	if match is None or len(match.groups()) != 4:
		print_warning(f"{title} has some non-captured properties. Regex does not working in it")
		return striped

	return f"{match.group(1)} - {match.group(4)}"


if __name__ == "__main__":
	main()


