from src.fs_manager import create_file_if_not_exist
from src.constants import ERROR_LOG, DEBUG_LOG
from src.logger import Logger
from logging import ERROR, DEBUG

def main():
    log = Logger.setup_logger("default", DEBUG_LOG, DEBUG)

if __name__ == "__main__":
    # from fs_manager.py
    create_file_if_not_exist(ERROR_LOG)
    create_file_if_not_exist(DEBUG_LOG)
    # from logger.py
    error_log = Logger.setup_logger("error", ERROR_LOG, ERROR)
    log = Logger.setup_logger("default", DEBUG_LOG, DEBUG)
    try:
        main()
    except KeyboardInterrupt as e:
        log.info("uscita in corso...")