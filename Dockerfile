# Dockerfile
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Expose port for the inference API
EXPOSE 8000

# Command to run the API server
CMD ["uvicorn", "src.inference_api:app", "--host", "0.0.0.0", "--port", "8000"]
