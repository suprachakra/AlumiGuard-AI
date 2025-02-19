#!/bin/bash
# jetson_tensorrt_build.sh
# Script to build a TensorRT-optimized Docker image for NVIDIA Jetson devices

DOCKER_IMAGE="jetson-tensorrt:latest"
docker build -f Dockerfile.jetson -t ${DOCKER_IMAGE} .
echo "TensorRT Docker image built: ${DOCKER_IMAGE}"
