import logging


def setup_logging():
    logging.basicConfig(
        filename="error.log",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
