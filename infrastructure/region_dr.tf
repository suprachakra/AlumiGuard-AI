# region_dr.tf
# Configuration for active-active replication and disaster recovery setup

resource "azurerm_key_vault" "kv" {
  name                = "defectDetectionKV"
  location            = var.region
  resource_group_name = "defect-detection-rg"
  sku_name            = "standard"
  tenant_id           = "your-tenant-id"
}

resource "azurerm_storage_account" "storage_dr" {
  name                     = "defectdetectiondr${var.region}"
  resource_group_name      = "defect-detection-rg"
  location                 = var.region
  account_tier             = "Standard"
  account_replication_type = "GRS"
}
