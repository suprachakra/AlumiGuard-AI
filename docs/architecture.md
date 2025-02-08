# System Architecture

## Overview:
The system consists of three layers:
1. **Edge Layer**: Real-time inference on NVIDIA Jetson AGX.
2. **Cloud Layer**: Model training and monitoring on Azure Kubernetes Service.
3. **Data Layer**: Centralized storage and analytics on Azure Synapse.

![System Architecture](diagrams/system_architecture.png)

## Data Pipeline:
- **Data Ingestion**: Images are ingested from smelters into Azure Blob Storage.
- **Data Processing**: Images are preprocessed and augmented using Azure Databricks.
- **Model Training**: Training occurs on Azure ML with data from Azure Blob Storage.
- **Inference**: Edge devices pull models from Azure Container Registry for real-time inference.

![Data Pipeline](diagrams/data_pipeline.png)
