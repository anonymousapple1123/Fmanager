# logger_conf.py
import logging


def setup_logging():
    logging.basicConfig(
        filename="error.log",  # Log file
        level=logging.ERROR,  # Log level
        format="%(asctime)s - %(levelname)s - %(message)s",  # Log message format
    )
