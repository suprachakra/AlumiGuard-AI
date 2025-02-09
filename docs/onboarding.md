# Onboarding & SOPs

## For DevOps
1. Clone repo, `cd AluminumDefectDetection`
2. `pip install -r requirements.txt`
3. See `scripts/deploy_azure.sh` for environment setup

## For Data Scientists
1. Explore `notebooks/defect_detection.ipynb`
2. Modify hyperparameters in `config/params.yaml`
3. Use `scripts/data_drift_detection.py` for drift analysis

## For QA Engineers
1. `pytest tests` for unit & integration
2. Load test via `locust -f tests/performance/test_load.py`
3. Coverage with `scripts/coverage.sh` (see `.coveragerc`)

## For Product Managers
- Refer to `docs/roadmap.md` & `docs/marketing_plan.md` for vision & milestones
- Collect feedback from pilot lines
