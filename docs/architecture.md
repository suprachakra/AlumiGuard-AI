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

## Technical Business Analysis & Translators

- **Business Needs Mapping**: We host regular sessions with product owners and domain experts to translate operational (OT) requirements into data & AI solutions.
- **Cross-Functional Coordination**: Technical business analysts facilitate communication between Data Science, IT/OT, and other stakeholders, ensuring consistent interpretation of business logic.
- **Documentation**: All discovered business logic is documented in an enterprise repository or architecture knowledge base, preventing misalignment.

## Solution Architecture Governance

- **Architecture Governance Board**: A team of architects oversees solution compliance with corporate standards, especially regarding IT/OT integration.
- **Blueprint & Roadmaps**: We maintain a “solution architecture blueprint” that evolves with new technologies or processes. 
- **Pre-Initiation Reviews**: All major projects pass an architecture checklist before starting, ensuring consistency and reducing system outages or mismatches.

## Cloud & Cost Management (FinOps)

- **Cloud Architecture**: Design scalable, secure solutions on Azure or multi-cloud. 
- **FinOps Collaboration**: We actively partner with FinOps to monitor usage, optimize compute/storage costs, and track ROI for each workload.
- **Application Performance Monitoring (APM)**: Performance metrics are aggregated in dashboards (Azure Monitor, Dynatrace, etc.) to quickly identify bottlenecks or cost overruns.
