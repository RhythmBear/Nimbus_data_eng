variable "resource_group_name" {
    type = string
    description = "Name of the resource gruop" 
    default = "nimbus-rg"
}

variable "resource_group_location" {
  type = string
  description = "Location of resource group to be created"
  default = "UK South"
}

variable "cluster_name" {
    type = string
    description = "Name given to the cluster"
    default = "nimbus-spark-cluster"
}

variable "storage_account_name" {
    type = string
    description = "Location of the cluster"
    default = "nimbussstorageaccounnt"
}

variable "container_name" {
    type = string
    description = "Name of the container"
    default = "nimbus-input"
}
