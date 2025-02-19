"""
test_train.py
-------------
Unit tests for training pipeline functions.
"""

import pytest
import torch
from src.models.model_utils import save_model, load_model

def test_model_save_and_load(tmp_path):
    # Create a dummy model (a simple tensor for illustration)
    dummy_model = {"weights": torch.randn(10, 10)}
    save_path = tmp_path / "dummy_model.pth"
    save_model(dummy_model, str(save_path))
    
    loaded_model = load_model("custom", str(save_path))
    # Basic test: ensure loaded model has the same keys
    assert "weights" in loaded_model
