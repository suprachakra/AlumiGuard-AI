# System Architecture

## Overview
AeroCheck AI is split into three layers:

1. **Edge Layer**: Real-time inference on NVIDIA Jetson AGX
2. **Cloud Layer**: Model training & orchestration on Azure (AKS + ACR)
3. **Data Layer**: Central data store in Azure Blob, analytics in Azure Synapse

![System Architecture](../diagrams/system_architecture.png)

## Data Pipeline
1. **Data Ingestion**: Images come from smelter lines or QA stations.
2. **Preprocessing**: Resize, augment, label in `data/labels/`.
3. **Model Training**: Done on Azure ML or custom GPU setups.
4. **Drift Detection**: `scripts/data_drift_detection.py` weekly checks.
5. **Edge Deployment**: YOLO models pulled from container registry.

![Data Pipeline](../diagrams/data_pipeline.png)

## Observability & Monitoring
- **Logging**: Centralized in Azure Monitor
- **Metrics**: GPU usage, inference latency
- **Alerting**: High error rates or unusual drift triggers ops notifications

## Monitoring & Alerting
- Integrate Azure Monitor or Datadog + Grafana
- Log ingestion: container logs => centralized platform
- Alerts: CPU usage > 80%, inference latency spike, sudden defect rate changes

