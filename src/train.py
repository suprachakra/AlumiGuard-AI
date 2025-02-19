"""
train.py
--------
Script to train the defect detection model.
Includes configuration loading, data pipeline setup, model training loop, and saving of artifacts.
"""

import os
import torch
import numpy as np
from src.data_processing import load_image, load_labels
from src.models.model_utils import load_model, save_model, evaluate_model
from src.utils.config_loader import load_config
from src.utils.logger import get_logger

logger = get_logger(__name__)

def train_model(config):
    # Load model (either a pre-trained YOLO or custom architecture)
    model = load_model(config["model"]["architecture"], config["model"]["pretrained_weights"])
    logger.info("Model loaded successfully.")

    # Load dataset (this example assumes a simple list of image paths and corresponding labels)
    image_paths = [os.path.join(config["data"]["raw_dir"], f) for f in os.listdir(config["data"]["raw_dir"]) if f.endswith('.jpg')]
    labels_df = load_labels(config["data"]["labels_csv"])
    logger.info(f"Found {len(image_paths)} images for training.")

    # Training loop (simplified example)
    epochs = config["training"]["epochs"]
    for epoch in range(epochs):
        losses = []
        for img_path in image_paths:
            image = load_image(img_path)
            image_proc = image / 255.0  # simple normalization
            # Forward pass, loss computation, backpropagation (placeholder)
            loss = np.random.uniform(0, 1)  # dummy loss
            losses.append(loss)
        avg_loss = np.mean(losses)
        logger.info(f"Epoch [{epoch+1}/{epochs}] - Loss: {avg_loss:.4f}")

    # Evaluate model performance
    metrics = evaluate_model(model, image_paths, labels_df)
    logger.info(f"Evaluation Metrics: {metrics}")

    # Save trained model
    save_model(model, config["model"]["save_path"])
    logger.info("Model training complete and saved.")

    return model, metrics

if __name__ == "__main__":
    config = load_config("config/params.yaml")
    train_model(config)
