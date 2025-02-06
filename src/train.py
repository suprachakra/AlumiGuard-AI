from ultralytics import YOLO
import yaml
import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    return logging.getLogger(__name__)

logger = setup_logger()

def train_model():
    try:
        with open('config/params.yaml', 'r') as f:
            config = yaml.safe_load(f)
        
        model = YOLO('models/yolov8n.pt')
        model.add_cbam(ratio=16)  # Add attention mechanism
        
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

