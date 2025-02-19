"""
test_negatives.py
-----------------
Tests for handling negative inputs such as corrupted images, truncated logs, and synthetic anomalies.
"""

import pytest
import numpy as np
from src.data_processing import preprocess_image

def test_corrupted_image():
    # Simulate a corrupted image (empty array)
    corrupted_image = np.array([])
    with pytest.raises(Exception):
        _ = preprocess_image(corrupted_image)

def test_incomplete_log():
    # Simulate a truncated log scenario in label CSV parsing
    import pandas as pd
    from io import StringIO
    truncated_csv = "label_id,defect_type,description\n1,crack"
    with pytest.raises(Exception):
        pd.read_csv(StringIO(truncated_csv))
