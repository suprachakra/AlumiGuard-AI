# Data Management

## Data Lifecycle
1. **Raw Data**: `data/raw/`
2. **Preprocessed**: Normalized, resized
3. **Labeled**: .csv with bounding boxes
4. **Augmented**: Synthetic transformations
5. **Versioned**: Tag each dataset with commit hashes or DVC
6. **Archived**: Long-term storage post-project

## Drift Monitoring
- **Weekly** with `scripts/data_drift_detection.py`
- Triggers partial retraining if drift above threshold (e.g., 0.2)

## Governance
- Access controlled via RBAC
- Regular backups to cold storage
- Automated data retention policy (e.g., 12 months online)

## Data Governance Policies

- **Governance Framework**: We adhere to a formal data governance framework that outlines roles (Data Stewards, Data Owners, etc.) and responsibilities.
- **Quality Assurance**: Define data quality checks, data lineage, and metadata management using tools like a Data Catalog (e.g., Apache Atlas, Collibra).
- **Privacy & Compliance**: Ensure PII or sensitive data is handled per GDPR and ISO 27001 guidelines. Access control with role-based permissions.
- **Hands-On Governance Platform**: We plan to roll out a data governance platform (e.g., Collibra, Alation) to unify data cataloging, lineage, and stewardship processes.

## Data Cataloging & Lineage

- **Data Catalog**: We maintain a centralized repository of data assets (data sources, tables, columns), plus business glossaries.
- **Lineage**: Automated lineage tracking to see how data flows from ingestion to ML models. This includes transformations, merges, and feature engineering steps.
- **Mapping**: Maintain a consistent “business logic to data” mapping. The Data Architect or “Go-To” person is responsible for ensuring domain definitions remain accurate.

## Data Management in MLOps

- **Coordination**: Act as a liaison between Data Engineering, MLOps, and Data Science for robust data pipelines and artifact versioning (DVC, MLflow, etc.).
- **Exploration & Governance**: Provide self-service analytics to business stakeholders (data exploration + standardized datasets).
- **Monitoring**: Regularly monitor data drift, schema changes, and quality anomalies to keep ML models accurate.

