from ultralytics import YOLO
import yaml
import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    return logging.getLogger(__name__)

logger = setup_logger()

def train_model():
    """
    Trains the YOLOv8 model based on config/params.yaml hyperparameters.
    Returns the trained model object.
    """
    try:
        with open('config/params.yaml', 'r') as f:
            config = yaml.safe_load(f)
        
        model = YOLO('models/yolov8n.pt')
        # If using a custom YOLO fork, optionally add CBAM or other modules
        # model.add_cbam(ratio=16)

        results = model.train(
            data='data/labels/defect_labels.csv',
            epochs=config['epochs'],
            imgsz=config['image_size'],
            batch=config['batch_size'],
            lr0=config['learning_rate']
        )
        logger.info("Training completed successfully")
        return model
    except Exception as e:
        logger.error(f"Training failed: {e}")
        raise
