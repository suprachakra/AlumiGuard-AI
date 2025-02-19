"""
test_inference_api.py
---------------------
Integration tests for the inference API endpoints using TestClient.
"""

from fastapi.testclient import TestClient
from src.inference_api import app

client = TestClient(app)

def test_predict_endpoint():
    # Create a dummy image (white square)
    import numpy as np
    import cv2
    dummy_img = 255 * np.ones((100, 100, 3), dtype=np.uint8)
    _, img_encoded = cv2.imencode('.jpg', dummy_img)
    response = client.post(
        "/predict",
        files={"file": ("dummy.jpg", img_encoded.tobytes(), "image/jpeg")}
    )
    assert response.status_code == 200
    json_resp = response.json()
    assert "detections" in json_resp
