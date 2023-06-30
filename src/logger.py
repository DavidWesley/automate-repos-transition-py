import logging

logger = logging.getLogger('Automator Repo Transitioning')
error_file_handler = logging.FileHandler(filename="automator-error.log", mode="a")
debug_file_handler = logging.FileHandler(filename="automator-debug.log", mode="a")
formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y/%m/%d %H:%M:%S')

logger.setLevel(logging.DEBUG)
error_file_handler.setLevel(logging.WARNING)
debug_file_handler.setLevel(logging.DEBUG)

error_file_handler.setFormatter(formatter)
debug_file_handler.setFormatter(formatter)

logger.addHandler(error_file_handler)
logger.addHandler(debug_file_handler)
