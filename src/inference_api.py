from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import logging
import os

from src.models.model_utils import DefectModel

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'CHANGE_IN_PROD')

limiter = Limiter(app=app, key_func=lambda: request.remote_addr)
jwt = JWTManager(app)

def setup_logger():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    return logging.getLogger(__name__)

logger = setup_logger()
model = DefectModel()

@app.route('/login', methods=['POST'])
def login():
    """
    Simple endpoint to obtain a JWT token.
    In production, integrate with your auth system.
    """
    data = request.json
    if data and data.get("username") == "test" and data.get("password") == "test123":
        token = create_access_token(identity={"user":"test"})
        return jsonify(access_token=token)
    return jsonify(error="Invalid credentials"), 401

@app.route('/predict', methods=['POST'])
@limiter.limit("100/minute")
@jwt_required()
def predict():
    """
    Main defect detection endpoint.
    Expects a multipart/form-data with 'image' field.
    Returns detected defects (type, confidence, bbox).
    """
    try:
        if 'image' not in request.files:
            return jsonify(error="No image provided"), 400
        
        image_bytes = request.files['image'].read()
        results = model.predict(image_bytes)
        return jsonify(results)
    except Exception as e:
        logger.error(f"API Error: {str(e)}")
        return jsonify(error="Internal error"), 500

if __name__ == "__main__":
    app.run(debug=True)
