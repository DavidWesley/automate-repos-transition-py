import logging

logger = logging.getLogger('Automator Repo Transitioning')
filehandler1 = logging.FileHandler(filename="automator-error.log", mode="a")
filehandler2 = logging.FileHandler(filename="automator-debug.log", mode="a")
formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y/%m/%d %H:%M:%S')

logger.setLevel(logging.DEBUG)
filehandler1.setLevel(logging.WARNING)
filehandler2.setLevel(logging.DEBUG)

filehandler1.setFormatter(formatter)
filehandler2.setFormatter(formatter)

logger.addHandler(filehandler1)
logger.addHandler(filehandler2)
