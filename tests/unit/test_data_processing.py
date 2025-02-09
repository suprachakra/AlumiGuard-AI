import pytest
import numpy as np
from src.data_processing import process_image, augment_image

def test_process_image_valid():
    # Assuming you have data/raw/sample_01.jpg
    img = process_image('data/raw/sample_01.jpg')
    assert img.shape == (640, 640, 3)

def test_process_image_invalid():
    with pytest.raises(ValueError):
        process_image('data/raw/non_existent.jpg')

def test_augment_image():
    dummy_image = np.zeros((640, 640, 3), dtype=np.uint8)
    augmented = augment_image(dummy_image)
    assert augmented.shape == (640, 640, 3)
