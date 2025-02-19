#!/bin/bash
# key_vault_integration.sh
# Script to integrate with Azure Key Vault for managing secrets

KEY_VAULT_NAME="defectDetectionVault"
az keyvault secret set --vault-name ${KEY_VAULT_NAME} --name "DBConnectionString" --value "YourConnectionStringHere"
echo "Secret stored in Azure Key Vault: ${KEY_VAULT_NAME}"
