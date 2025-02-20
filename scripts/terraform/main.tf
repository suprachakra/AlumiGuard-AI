# main.tf
# Terraform configuration for deploying the infrastructure components

provider "azurerm" {
  features = {}
}

resource "azurerm_resource_group" "rg" {
  name     = "defect-detection-rg"
  location = "eastus"
}

resource "azurerm_storage_account" "storage" {
  name                     = "defectdetectionstorage"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "GRS"
}
