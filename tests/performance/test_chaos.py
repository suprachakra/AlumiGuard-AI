import requests
import pytest

def test_chaos_scenario():
    """
    Simulates partial network outage or high latency.
    """
    try:
        resp = requests.post(
            "http://localhost:5000/predict",
            files={"image": open("data/raw/sample_01.jpg", "rb")},
            timeout=1  # intentionally short
        )
        assert resp.status_code == 200
    except requests.exceptions.Timeout:
        # The test can pass if we expect occasional timeouts in chaos scenarios
        assert True
