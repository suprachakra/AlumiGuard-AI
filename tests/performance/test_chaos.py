"""
test_chaos.py
-------------
Chaos tests to simulate unexpected system stress and component failures.
"""

import pytest
from src.inference_api import run_inference
import numpy as np

def test_chaos_injection():
    # Create a corrupted image (simulate noise)
    corrupted_img = np.random.randint(0, 256, (640, 640, 3), dtype=np.uint8)
    try:
        detections = run_inference(corrupted_img)
        # Even if the image is noisy, the system should not crash
        assert isinstance(detections, list)
    except Exception as e:
        pytest.fail(f"Inference failed under chaos conditions: {e}")
