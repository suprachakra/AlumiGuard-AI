#!/bin/bash
# deploy_azure.sh
# Script to deploy the application to Azure AKS

RESOURCE_GROUP="rg-defect-detection"
CLUSTER_NAME="defect-detection-cluster"
echo "Deploying to Azure AKS cluster ${CLUSTER_NAME} in resource group ${RESOURCE_GROUP}..."
az aks get-credentials --resource-group ${RESOURCE_GROUP} --name ${CLUSTER_NAME}
kubectl apply -f scripts/terraform/main.tf
echo "Deployment initiated."
