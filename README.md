# AlumiGuard-AI
Defending Quality in Aluminum Manufacturing with Machine Precision and AI-Powered Perfection. it automates detection of aluminum surface defects (cracks, corrosion, pitting, dents). It leverages YOLOv8, containerized microservices, and can run on NVIDIA Jetson or in the cloud.

# Aluminum Defect Detection System

## Overview

This project uses YOLOv8 to detect surface defects and forging a new era of automated quality in aluminum manufacturing


## Features:
1. **Real-time defect detection API** with 94.7% mAP.
2. **Pretrained YOLOv8 model** integration with CBAM attention mechanism.
3. **Dockerized deployment** for scalability and ease of use.
4. **SAFe Agile implementation** for iterative development.
5. **Azure integration** for cloud scalability and security.
6. **Compliance with ISO 27001 and GDPR**.
7. **Runtime encryption** for model weights.

## Quick Start:
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the API: `python src/inference_api.py`.
4. Test the API using Postman or cURL.

## SAFe Agile Metrics:
- **2-Week Sprint Cycles**
- **98% Automation Coverage**
- **$120M/3yr Projected ROI**
> Refer [Roadmap](https://github.com/suprachakra/AlumiGuard-AI/blob/main/docs/roadmap.md#phase-1-foundation--pilot-months-03)

```mermaid
flowchart TB
 subgraph ICS_Env["**ICS & Edge Layer**"]
    direction TB
        A1["ICS Security Tools<br>Nozomi\/Vectra"]
        A2["PLCs, SCADA,<br>Thermal Cameras"]
        A3["NVIDIA Jetson HPC<br>(Local YOLO)"]
        A4["Offline Buffer<br>& Fallback"]
        A5["ICS DMZ<br>(Firewall\/WAF)"]
  end
 subgraph Azure_Cloud["**Azure Cloud Services & MLOps**"]
    direction TB
        B1["AKS<br>(Kubernetes + CNCF)"]
        B2["Data Preprocessing<br>& Validation"]
        B3["MLOps Pipeline<br>(Tekton\/Jenkins)"]
        B4["Model Registry<br>(ACR\/MLflow)"]
        B5["Azure Machine Learning<br>(Training,<br>Hyperparam Tuning)"]
        B6["Observability<br>(Prometheus\/Azure Monitor)"]
        B7["Logs<br>(Loki\/LogAnalytics)"]
        B8["Multi-Region Setup<br>(HA\/DR)"]
  end
 subgraph Data_and_Compliance["**Data Governance & Compliance**"]
    direction TB
        C1["Azure Blob\/ADLS<br>(Raw Images, ICS Logs)"]
        C2["Azure Synapse\/Databricks<br>(Advanced Analytics)"]
        C3["Purview\/Collibra<br>(Lineage,<br>Catalog)"]
        C4["Key Vault<br>(Secrets,<br>Encryption)"]
        C5["ISO 27001\/GDPR Tools<br>Retention & Audits"]
  end
 subgraph QA_Brand_Marketing["**QA, Brand & Marketing**"]
        D1["QA & Negative Testing<br>Corrupted images,<br>Chaos scripts"]
        D2["Operator UI\/UX<br>Feedback Loop"]
        D3["Brand Identity<br>(Name, Logo,<br>Messaging)"]
        D4["Marketing & Comms<br>(Whitepapers,<br>ROI Demos)"]
  end
 subgraph Stakeholders["**Key Stakeholders & Cross-Functional Teams**"]
        E1["SVP Product Mgmt"]
        E2["SVP Engineering"]
        E3["SVP Data"]
        E4["SVP QA"]
        E5["SVP Brand\/Marketing"]
        E6["SVP Design"]
        E7["SVP Other XFn Teams"]
  end
    A2 -- Images & ICS data --> A3
    A3 -- Local Inference --> A4
    A1 -- Threat logs --> A5
    A3 -- Defect Metadata --> A5
    B1 --> B2 & B3 & B6 & B8
    B3 --> B4 & B5
    B6 --> B7
    C1 --> C2 & C3
    C2 -- "Predictive Maintenance,<br>Time-series Analysis" --> C3
    C3 --> C5
    C4 --> C5
    D1 --> D2
    D3 --> D4
    E1 --- E2
    E2 --- E3
    E3 --- E4
    E4 --- E5
    E5 --- E6
    E6 --- E7
    A5 -- Secure Transfer --> B1
    B1 -- Processed Data,<br>Model Artifacts --> C1
    B1 -- Logs & Observability --> C2
    B4 -- Deployed Containers --> A3
    B1 -- QA & CI Pipeline --> D1
    D2 -- User Feedback,<br>Labeling --> B2
    D3 -- "Product Marketing,<br>Go-to-Market" --> E1
    D4 -- ROI Demos,<br>Whitepapers --> E1
    B8 -- DR & HA Strategy --> C1
    E1 -- Roadmap & Epics --> B1
    E2 -- Engineering Oversight --> B1
    E3 -- Data Governance,<br>Analytics Strategy --> C3
    E4 -- Test Coverage,<br>UAT Approval --> D1
    E5 -- Brand Comms,<br>Fairs & Summits --> D4
    E6 -- UX Prototypes,<br>Operator Dash --> D2
    E7 -- Finance,<br>Legal,<br>Procurement --> C5

     A1:::ICS
     A2:::ICS
     A3:::HPC
     A4:::HPC
     A5:::DMZ
     B1:::Azure
     B2:::Azure
     B3:::MLOps
     B4:::MLOps
     B5:::MLOps
     B6:::Azure
     B7:::Azure
     B8:::Azure
     C1:::Azure
     C2:::Azure
     C3:::Gov
     C4:::Azure
     C5:::Gov
     D1:::QA
     D2:::QA
     D3:::Brand
     D4:::Brand
     E1:::Stakeholder
     E2:::Stakeholder
     E3:::Stakeholder
     E4:::Stakeholder
     E5:::Stakeholder
     E6:::Stakeholder
     E7:::Stakeholder
    classDef ICS fill:#fee7e7,stroke:#eb9d9d,color:#701414
    classDef HPC fill:#f7f1e7,stroke:#d8b862,color:#5a4d1f
    classDef DMZ fill:#fff8e7,stroke:#e8c96f,color:#5f4509
    classDef Azure fill:#e7f0fe,stroke:#8daee9,color:#0f1d55
    classDef MLOps fill:#f2eafa,stroke:#c7b5ea,color:#401e73
    classDef Gov fill:#eafce7,stroke:#9fd79f,color:#22532f
    classDef Brand fill:#fce7fa,stroke:#d79fd4,color:#531f45
    classDef QA fill:#fefbd0,stroke:#dad169,color:#5a5c09
    classDef Stakeholder fill:#f3ffe7,stroke:#bdde89,color:#3a4c1f
    style ICS_Env fill:transparent,stroke:#FF6D00
    style Azure_Cloud fill:transparent,stroke:#AA00FF
    style QA_Brand_Marketing fill:transparent,stroke:#00C853
    style Data_and_Compliance fill:transparent,stroke:#2962FF
    style Stakeholders fill:transparent,stroke:#D50000
```

