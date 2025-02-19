```mermaid
graph TD
    A[Edge Devices Jetson HPC] --> B[ICS Network]
    B --> C[Cloud Ingestion  AKS ]
    C --> D[Microservices  Inference API ]
    D --> E[Operator Dashboard]
    D --> F[Data Lake & Analytics]
    F --> G[Predictive Maintenance Module]
```
