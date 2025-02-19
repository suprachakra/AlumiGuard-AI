"""
inference_api.py
----------------
Provides a RESTful API for performing inference on new images.
Uses FastAPI for handling requests and returns defect detections in JSON format.
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
import cv2
import numpy as np
from io import BytesIO
from src.models.model_utils import load_model, predict
from src.utils.config_loader import load_config
from src.utils.logger import get_logger

logger = get_logger(__name__)
app = FastAPI(title="Defect Detection Inference API", version="1.0")

# Load configuration and model at startup
config = load_config("config/params.yaml")
model = load_model(config["model"]["architecture"], config["model"]["save_path"])

@app.post("/predict")
async def predict_defects(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError("Invalid image file.")
    except Exception as e:
        logger.error(f"Error processing image: {e}")
        raise HTTPException(status_code=400, detail="Invalid image file.")
    
    # Run prediction
    detections = predict(model, image)
    return {"detections": detections}

def run_inference(image):
    """
    Helper function to run inference on a given image.
    Returns a list of detections.
    """
    return predict(model, image)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
