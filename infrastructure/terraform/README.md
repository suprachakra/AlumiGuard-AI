# Terraform IaC for AlumiGuard AI

## Purpose
This folder contains Terraform modules to provision:
- Azure Resource Group
- Azure Container Registry (ACR)
- Azure Kubernetes Service (AKS)

## Usage
1. Set variables in `variables.tf` or a `.tfvars` file
2. Initialize: `terraform init`
3. Plan: `terraform plan -out tfplan`
4. Apply: `terraform apply tfplan`

## Next Steps
- Integrate Key Vault, Azure Monitor, and other services
- Scale node pools for large deployments
