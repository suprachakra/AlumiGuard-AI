import pytest
from src.train import train_model

def test_train_model():
    model = train_model()
    assert model is not None
    # Optionally check if model files got updated or if training stats are valid
