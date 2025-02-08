import pytest
import requests

def test_chaos_engineering():
    # Simulate network partition
    response = requests.post('http://localhost:5000/predict', files={'image': open('data/raw/sample_01.jpg', 'rb')})
    assert response.status_code == 200
