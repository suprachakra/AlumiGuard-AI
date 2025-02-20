# outputs.tf
output "storage_account_primary_endpoint" {
  value = azurerm_storage_account.storage.primary_blob_endpoint
}
