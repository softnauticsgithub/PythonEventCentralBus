import logging
from config.constants import LOG_LEVEL

# TODO: Add file handler if needed
def get_logger(name="router"):
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    if not logger.handlers:
        ch = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        )
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger