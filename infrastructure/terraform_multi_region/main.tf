# main.tf
# Terraform configuration for multi-region high availability

provider "azurerm" {
  features = {}
}

module "primary_region" {
  source = "./region"
  region = "eastus"
}

module "secondary_region" {
  source = "./region"
  region = "westus"
}
