## API Documentation

### Endpoints

#### POST /login
- **Description**: Obtain a JWT token by providing credentials (`username`, `password`).

#### POST /predict
- **Description**: Upload an image for defect detection.
- **Headers**: `Authorization: Bearer <token>`
- **Payload**: `multipart/form-data` with an `image` field.
- **Response**:
  ```json
  {
    "detections": [
      {
        "defect_type": "crack",
        "confidence": 0.92,
        "bbox": [50, 100, 200, 300]
      }
    ]
  }
