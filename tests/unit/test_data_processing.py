"""
test_data_processing.py
-----------------------
Unit tests for data_processing.py functions.
"""

import os
import cv2
import pytest
import numpy as np
from src.data_processing import load_image, preprocess_image, augment_image

def test_load_image(tmp_path):
    # Create a temporary dummy image
    dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
    temp_img_path = tmp_path / "dummy.jpg"
    cv2.imwrite(str(temp_img_path), dummy_image)
    
    img = load_image(str(temp_img_path))
    assert img is not None
    assert img.shape == (100, 100, 3)

def test_preprocess_image():
    dummy_image = np.ones((200, 200, 3), dtype=np.uint8) * 255
    processed = preprocess_image(dummy_image, target_size=(640, 640))
    assert processed.shape == (640, 640, 3)
    assert processed.max() <= 1.0

def test_augment_image():
    dummy_image = np.ones((100, 100, 3), dtype=np.uint8) * 128
    augmented = augment_image(dummy_image)
    # Check that output is still a valid image array
    assert augmented.shape == dummy_image.shape
