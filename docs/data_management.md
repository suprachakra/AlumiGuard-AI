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
