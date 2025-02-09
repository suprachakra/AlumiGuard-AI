#!/bin/bash
# Sample script to pull secrets from Azure Key Vault

VAULT_NAME="myKeyVault"
SECRET_NAME="JWT_SECRET_KEY"

echo "Retrieving $SECRET_NAME from $VAULT_NAME..."
SECRET_VALUE=$(az keyvault secret show --vault-name $VAULT_NAME --name $SECRET_NAME --query value -o tsv)

export JWT_SECRET_KEY=$SECRET_VALUE
echo "Exported JWT_SECRET_KEY from Key Vault."
