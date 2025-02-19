#!/bin/bash
# docker_build.sh
# Script to build the Docker image for the defect detection application

IMAGE_NAME="defect-detection:latest"
docker build -t ${IMAGE_NAME} .
echo "Docker image ${IMAGE_NAME} built successfully."
