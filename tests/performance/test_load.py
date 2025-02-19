"""
test_load.py
------------
Performance tests to measure load times and throughput of the system.
"""

import time
import cv2
import numpy as np
from src.inference_api import run_inference

def test_inference_performance():
    # Generate a dummy image
    dummy_img = 255 * np.ones((640, 640, 3), dtype=np.uint8)
    
    start_time = time.time()
    detections = run_inference(dummy_img)
    end_time = time.time()
    
    duration = end_time - start_time
    # Assert that inference takes less than 0.05 seconds (50ms)
    assert duration < 0.05
