import pytest
from src.data_processing import process_image, augment_image

def test_process_image():
    assert process_image('data/raw/sample_01.jpg') is not None

def test_augment_image():
    image = process_image('data/raw/sample_01.jpg')
    augmented = augment_image(image)
    assert augmented.shape == image.shape
