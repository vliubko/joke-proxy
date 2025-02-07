import logging
from pythonjsonlogger import jsonlogger

def setup_logging():
    # Check if logger is already configured
    if logging.getLogger().handlers:
        return logging.getLogger()

    logger = logging.getLogger()
    logHandler = logging.StreamHandler()

    formatter = jsonlogger.JsonFormatter(
        '%(asctime)s %(levelname)s %(message)s'
    )
    logHandler.setFormatter(formatter)

    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)

    return logger
