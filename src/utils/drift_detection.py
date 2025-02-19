"""
drift_detection.py
------------------
Module to detect data drift between training and live data streams.
Uses statistical tests (e.g., Kolmogorov-Smirnov) to flag significant changes.
"""

import numpy as np
from scipy.stats import ks_2samp
from src.utils.logger import get_logger

logger = get_logger(__name__)

def detect_drift(train_data: np.ndarray, live_data: np.ndarray, alpha=0.05) -> bool:
    """
    Compare distributions of training and live data using the KS test.
    Returns True if drift is detected.
    """
    stat, p_value = ks_2samp(train_data, live_data)
    logger.info(f"KS Test: statistic={stat:.4f}, p_value={p_value:.4f}")
    drift = p_value < alpha
    if drift:
        logger.warning("Data drift detected!")
    else:
        logger.info("No significant data drift detected.")
    return drift

if __name__ == "__main__":
    train = np.random.normal(0, 1, 1000)
    live = np.random.normal(0, 1, 1000)
    detect_drift(train, live)
