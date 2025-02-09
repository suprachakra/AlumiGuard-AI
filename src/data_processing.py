import cv2
import albumentations as A
import numpy as np

def process_image(image_path):
    """
    Reads and resizes an image to 640x640 resolution.
    Raises an exception if the file is invalid or cannot be read.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not read image from {image_path}")
    return cv2.resize(image, (640, 640))

def augment_image(image):
    """
    Applies a series of augmentations to the image for diversity.
    """
    pipeline = A.Compose([
        A.RandomBrightnessContrast(p=0.5),
        A.HorizontalFlip(p=0.5),
        A.CLAHE(p=0.3),
        A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.1, rotate_limit=45, p=0.5),
        A.GaussNoise(p=0.2),
        A.Blur(blur_limit=3, p=0.3),
        A.RandomGamma(p=0.3)
    ])
    return pipeline(image=image)['image']

def generate_synthetic_defects(image):
    """
    Placeholder for advanced synthetic defect generation, e.g., overlay crack textures.
    """
    # Sample approach: random overlay, morphological operations, etc.
    return image
