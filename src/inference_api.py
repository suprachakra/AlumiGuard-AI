from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_jwt_extended import JWTManager, jwt_required
import logging
import os
from src.models.model_utils import DefectModel
from src.utils.encryption import encrypt_weights, decrypt_weights

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'CHANGE_IN_PROD')
limiter = Limiter(app=app, key_func=lambda: request.remote_addr)
jwt = JWTManager(app)

def setup_logger():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    return logging.getLogger(__name__)

logger = setup_logger()

model = DefectModel()

@app.route('/predict', methods=['POST'])
@limiter.limit("100/minute")
@jwt_required()
def predict():
    try:
        if 'image' not in request.files:
            return jsonify(error="No image provided"), 400
        
        image = request.files['image'].read()
        results = model.predict(image)
        return jsonify({
            "defect_type": results['defect_type'],
            "confidence": results['confidence'],
            "bbox": results['bbox'],
            "plant": results['plant']
        })
    except Exception as e:
        logger.error(f"API Error: {str(e)}")
        return jsonify(error="Internal error"), 500

if __name__ == '__main__':
    app.run(debug=True)
