import logging
from colorama import Fore, Style

path_to_logs = "" # path log
terminal_cleanup_command = 'clear'

def info_(text: str) -> str:
    "info message"
    logger.info(text)

def warning_(text: str) -> str:
    "warning message"
    logger.warning(text)

def error_(text: str) -> str:
    "error message"
    logger.error(text)

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s : %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.propagate = False
logger.addHandler(console_handler)
logging.addLevelName(logging.INFO, f"[{Fore.GREEN}{logging.getLevelName(logging.INFO)}{Style.RESET_ALL}]")
logging.addLevelName(logging.WARNING, f"[{Fore.YELLOW}{logging.getLevelName(logging.WARNING)}{Style.RESET_ALL}]")
logging.addLevelName(logging.ERROR, f"[{Fore.RED}{logging.getLevelName(logging.ERROR)}{Style.RESET_ALL}]")
logging.basicConfig(filename=f"{path_to_logs}logs.txt",
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG)