import logging
import os

def get_logger():
    logger = logging.getLogger()
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()  # デフォルトは INFO
    logger.setLevel(getattr(logging, log_level, logging.INFO))
    return logger