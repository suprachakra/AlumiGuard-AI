"""
data_processing.py
------------------
Module for processing raw data into a format suitable for training and inference.
Includes functions for image pre-processing, augmentation, and label parsing.
"""

import os
import cv2
import numpy as np
import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__)

def load_image(image_path):
    """Load an image from disk."""
    logger.debug(f"Loading image from: {image_path}")
    image = cv2.imread(image_path)
    if image is None:
        logger.error(f"Failed to load image at {image_path}")
        raise FileNotFoundError(f"Image not found: {image_path}")
    return image

def preprocess_image(image, target_size=(640, 640)):
    """
    Preprocess the image:
    - Resize to target size.
    - Normalize pixel values.
    """
    logger.debug("Preprocessing image")
    resized = cv2.resize(image, target_size)
    normalized = resized / 255.0
    return normalized

def augment_image(image):
    """
    Apply data augmentation techniques:
    - Horizontal flip
    - Random brightness/contrast adjustments
    """
    logger.debug("Augmenting image")
    # Horizontal flip
    flipped = cv2.flip(image, 1)
    # Adjust brightness/contrast
    alpha = np.random.uniform(0.9, 1.1)  # contrast control
    beta = np.random.uniform(-10, 10)    # brightness control
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted

def load_labels(csv_path):
    """Load defect labels from CSV."""
    logger.debug(f"Loading labels from: {csv_path}")
    try:
        df = pd.read_csv(csv_path)
        return df
    except Exception as e:
        logger.error(f"Error loading labels: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    img = load_image("data/raw/sample_image.jpg")
    proc_img = preprocess_image(img)
    aug_img = augment_image(proc_img)
    labels = load_labels("data/labels/defect_labels.csv")
    logger.info("Data processing module executed successfully.")
