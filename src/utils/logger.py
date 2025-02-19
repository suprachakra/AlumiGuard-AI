"""
logger.py
---------
Configures and returns a standardized logger for the application.
"""

import logging
import sys

def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        # Configure handler if not already configured
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(name)s: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    return logger

if __name__ == "__main__":
    log = get_logger("TestLogger")
    log.info("Logger is configured properly.")
