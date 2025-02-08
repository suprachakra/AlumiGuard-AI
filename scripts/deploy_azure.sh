#!/bin/bash

az login
az acr login --name <acr-name>

docker tag aluminum-defect-detection:latest <acr-name>.azurecr.io/aluminum-defect-detection:latest

docker push <acr-name>.azurecr.io/aluminum-defect-detection:latest

az aks get-credentials --resource-group <resource-group> --name <aks-cluster-name>

kubectl apply -f kubernetes/deployment.yaml
