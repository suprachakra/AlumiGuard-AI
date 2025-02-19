"""
config_loader.py
----------------
Utility to load configuration parameters from a YAML file.
"""

import yaml
from src.utils.logger import get_logger

logger = get_logger(__name__)

def load_config(config_path: str) -> dict:
    """Load and return configuration from the specified YAML file."""
    logger.info(f"Loading configuration from {config_path}")
    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        logger.debug(f"Configuration loaded: {config}")
        return config
    except Exception as e:
        logger.error(f"Error loading config: {e}")
        raise

if __name__ == "__main__":
    config = load_config("config/params.yaml")
    logger.info("Configuration loaded successfully.")
