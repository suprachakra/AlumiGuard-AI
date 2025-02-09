import cv2
import numpy as np
from ultralytics import YOLO

class DefectModel:
    """
    Wrapper class for YOLO inference and post-processing logic.
    """

    def __init__(self, model_path='models/custom_model.pth'):
        try:
            self.model = YOLO(model_path)
        except:
            # fallback if custom weights aren't available
            self.model = YOLO('models/yolov8n.pt')

    def predict(self, image_bytes):
        # Convert the bytes to a numpy array
        image_array = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError("Invalid image data provided")

        # YOLO inference
        results = self.model.predict(source=image, conf=0.25)

        # Collate detections
        output = []
        if len(results) > 0:
            for det in results[0].boxes:
                output.append({
                    "defect_type": "crack",  # placeholder classification logic
                    "confidence": float(det.conf[0]),
                    "bbox": det.xyxy[0].tolist()
                })
        return {"detections": output}
