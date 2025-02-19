#!/usr/bin/env python3
"""
data_validation.py
------------------
Script to validate data quality and consistency.
"""

import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__)

def validate_labels(csv_path):
    try:
        df = pd.read_csv(csv_path)
        if df.isnull().sum().sum() > 0:
            logger.warning("Missing values found in labels CSV.")
        else:
            logger.info("Labels CSV validated successfully.")
    except Exception as e:
        logger.error(f"Error validating labels: {e}")
        raise

if __name__ == "__main__":
    validate_labels("data/labels/defect_labels.csv")
