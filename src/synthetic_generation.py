"""
synthetic_generation.py
-----------------------
Module to generate synthetic defect images using a GAN approach.
Helps augment the training dataset when real defect samples are scarce.
"""

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, Model
from src.utils.logger import get_logger

logger = get_logger(__name__)

def build_generator(latent_dim=100):
    """Builds the generator model."""
    model = tf.keras.Sequential(name="Generator")
    model.add(layers.Dense(8 * 8 * 256, input_dim=latent_dim))
    model.add(layers.LeakyReLU(alpha=0.2))
    model.add(layers.Reshape((8, 8, 256)))
    
    model.add(layers.Conv2DTranspose(128, kernel_size=4, strides=2, padding="same"))
    model.add(layers.LeakyReLU(alpha=0.2))
    
    model.add(layers.Conv2DTranspose(64, kernel_size=4, strides=2, padding="same"))
    model.add(layers.LeakyReLU(alpha=0.2))
    
    model.add(layers.Conv2DTranspose(3, kernel_size=4, strides=2, padding="same", activation="tanh"))
    logger.info("Generator model built.")
    return model

def generate_synthetic_image(generator, latent_dim=100):
    """Generates a single synthetic defect image."""
    noise = np.random.normal(0, 1, (1, latent_dim))
    synthetic_image = generator.predict(noise)
    # Rescale image to [0, 255]
    synthetic_image = ((synthetic_image + 1) * 127.5).astype("uint8")
    return synthetic_image[0]

if __name__ == "__main__":
    latent_dim = 100
    generator = build_generator(latent_dim)
    synthetic_img = generate_synthetic_image(generator, latent_dim)
    # Save synthetic image for review
    tf.keras.preprocessing.image.save_img("data/raw/synthetic_defect.jpg", synthetic_img)
    logger.info("Synthetic defect image generated and saved.")
