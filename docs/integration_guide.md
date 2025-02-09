# Integration Guide (ERP/MES)

## Purpose
Explain how to integrate AeroCheck AI with standard manufacturing systems.

## Steps
1. **Obtain JWT** from /login
2. **Call /predict** for each image or batch
3. **Parse JSON** and update ERP records (SAP, Oracle, etc.)

## Sample Code (Python snippet)
```python
import requests

def detect(image_path, token):
    files = {"image": open(image_path, "rb")}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post("http://localhost:5000/predict", files=files, headers=headers)
    return response.json()
```

## Error Handling
Rate limit (429): Retry logic
500: Fallback to manual inspection
Invalid image: Alert user in ERP UI

## Future Enhancements
Webhooks for asynchronous notifications
Bulk/batch endpoints for large volumes
