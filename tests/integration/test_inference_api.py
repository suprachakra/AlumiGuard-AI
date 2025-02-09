import requests
import pytest

BASE_URL = "http://localhost:5000"

def test_login_and_predict():
    # 1) Login
    login_resp = requests.post(f"{BASE_URL}/login", json={"username":"test","password":"test123"})
    assert login_resp.status_code == 200
    token = login_resp.json().get("access_token")
    assert token is not None

    # 2) Predict
    headers = {"Authorization": f"Bearer {token}"}
    files = {"image": open("data/raw/sample_01.jpg","rb")}
    resp = requests.post(f"{BASE_URL}/predict", files=files, headers=headers)
    assert resp.status_code == 200
    response_json = resp.json()
    assert "detections" in response_json
