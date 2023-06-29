from logger import logger
from colors import ANSIColors


def print_info(message: str, end: str | None = None) -> None:
	if end is None:
		end = "\n"

	logger.info(message)
	print(f"{ANSIColors.BLUE}{ANSIColors.BOLD}INFO:{ANSIColors.BOLD}", end="\t")
	print(f"{ANSIColors.BLUE}{message}\t{ANSIColors.RESET}", end=end)


def print_err(message: str, end: str | None = None) -> None:
	if end is None:
		end = "\n"

	logger.error(message)
	print(f"{ANSIColors.RED}{ANSIColors.BOLD}ERROR:{ANSIColors.BOLD}", end="\t")
	print(f"{ANSIColors.RED}{message}\t{ANSIColors.RESET}", end=end)


def print_warning(message: str, end: str | None = None) -> None:
	if end is None:
		end = "\n"

	logger.warning(message)
	print(f"{ANSIColors.YELLOW}{ANSIColors.BOLD}WARNING:{ANSIColors.BOLD}", end="\t")
	print(f"{ANSIColors.YELLOW}{message}\t{ANSIColors.RESET}", end=end)


def print_header(message: str, end: str | None = None) -> None:
	if end is None:
		end = "\n"

	print(f"{ANSIColors.UNDERLINE}{ANSIColors.BOLD}{message}\t{ANSIColors.RESET}", end=end)

def print_debug(message: str) -> None:
	logger.debug(message)
