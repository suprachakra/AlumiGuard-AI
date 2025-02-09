FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the Flask API port
EXPOSE 5000

CMD ["python", "src/inference_api.py"]
