import requests
import pytest

def test_predict_endpoint():
    response = requests.post('http://localhost:5000/predict', files={'image': open('data/raw/sample_01.jpg', 'rb')})
    assert response.status_code == 200
    assert 'confidence' in response.json()

def test_api_rate_limit():
    for _ in range(101):
        response = requests.post('http://localhost:5000/predict', files={'image': open('data/raw/sample_01.jpg', 'rb')})
    assert response.status_code == 429  # Too Many Requests
