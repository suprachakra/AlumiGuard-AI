variable "resource_group_name" {
  type        = string
  description = "Name of the Azure Resource Group."
}

variable "location" {
  type        = string
  description = "Azure region for resources."
  default     = "eastus"
}

variable "acr_name" {
  type        = string
  description = "Name of Azure Container Registry."
}

variable "aks_name" {
  type        = string
  description = "Name of the AKS cluster."
}

variable "aks_dns_prefix" {
  type        = string
  description = "DNS prefix for AKS."
}

variable "node_count" {
  type        = number
  description = "Number of nodes in the AKS cluster."
  default     = 3
}

variable "vm_size" {
  type        = string
  description = "VM size for the AKS cluster nodes."
  default     = "Standard_DS2_v2"
}
