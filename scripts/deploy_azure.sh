#!/bin/bash
# Azure Deployment Script (simplistic example)

# Login to Azure
az login

# ACR Login
ACR_NAME="<acr-name>"
az acr login --name $ACR_NAME

# Build & Push
docker tag aerocheck-ai:latest $ACR_NAME.azurecr.io/aerocheck-ai:latest
docker push $ACR_NAME.azurecr.io/alumiguard-ai:latest

# AKS Deployment
RESOURCE_GROUP="<resource-group>"
AKS_NAME="<aks-cluster-name>"

az aks get-credentials --resource-group $RESOURCE_GROUP --name $AKS_NAME
kubectl apply -f kubernetes/deployment.yaml
