import logging

def setup_logger():
    """
    Set up a simple logger for the system.
    """
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    return logging.getLogger(__name__)
