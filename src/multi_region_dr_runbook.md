## Multi-Region DR Runbook
This runbook describes how to simulate a regional outage and ensure our ICS + HPC + Azure MLOps solution continues running in the secondary region with minimal downtime.

---
### Prerequisites
1. **Terraform** or **Bicep** scripts for both primary and secondary Azure regions.
2. **Geo-Redundant Storage (GRS)** for ADLS/Blob.
3. **Secondary AKS** cluster with minimal node count.
4. **Replicated Key Vault** or Key Vault references in secondary region.
5. DNS or traffic manager to fail over the API Gateway endpoint.

---
### DR Test Steps

#### 1. Pre-Test Checks
- **Confirm** Terraform deployment in both regions:
  - `terraform plan -var-file=region1.tfvars` for primary
  - `terraform plan -var-file=region2.tfvars` for secondary
- **Verify** GRS replication is healthy (Azure portal -> Storage accounts -> Replication status).
- **Ensure** secondary AKS cluster is up to date with microservice images (Argo CD or Flux should be in sync).

#### 2. Initiate Outage in Primary Region
- **Simulate** a region-level outage by:
  - Stopping or scaling primary AKS node pool to zero,
  - or disabling inbound traffic in primary region’s firewall,
  - or forcibly removing primary region from traffic manager’s DNS routing.

### 3. Validate Secondary Region
- **Check** if secondary region’s AKS cluster automatically scales up:
  - If using auto-scaling, it should detect new traffic and spin up nodes.
  - If manual scaling, run `az aks scale` or Terraform to set desired node count.
- **Monitor** the ICS data flow:
  - HPC edge devices should re-route to the secondary region’s API gateway if DNS is updated or if a fallback domain is configured.
- **Confirm** microservices are healthy (`kubectl get pods -n <namespace>`).
- **Ensure** Key Vault secrets in secondary region are accessible by microservices.

#### 4. Test ICS & HPC Flows
- **Generate** some new defect images from HPC edge to see if they arrive in the secondary ADLS container.
- **Run** YOLO inference or MLOps pipeline triggers to confirm partial functionality remains.

#### 5. Observability & Metrics
- **Review** Prometheus/Grafana or Azure Monitor in the secondary region:
  - Check CPU usage, memory usage, request counts.
- **Validate** logs in secondary region’s Log Analytics or Loki.

#### 6. Rollback / Return to Primary
- Once the test is complete, re-enable the primary region:
  - Scale AKS node pool back,
  - Re-enable firewall rules,
  - Switch traffic manager DNS back to primary.
- Confirm that data re-syncs from GRS to the primary region if any new data was generated.

---
### Success Criteria
- **RTO < 1 Hour**: The solution is fully operational in the secondary region within 60 minutes.
- **No Data Loss**: GRS ensures no missed ICS logs or HPC defect data.
- **Minimal HPC Disruption**: HPC can route to the secondary region’s gateway seamlessly.

---
### Common Pitfalls & Mitigations
- **DNS TTL** too long -> use short TTL (e.g., 60s) for traffic manager.
- **Missing secrets** in secondary Key Vault -> ensure replication or re-import is done pre-test.
- **Under-provisioned secondary AKS** -> have at least 1-2 nodes running at all times or use cluster auto-scaler.

---
## Post-Test Actions
- Document all findings in Confluence or SharePoint.
- Update runbook if any manual steps can be automated.
- Share success metrics with cross-functional teams (Product, ICS Eng, Security).
