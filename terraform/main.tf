data "azurerm_client_config" "current" {}

resource "azurerm_resource_group" "nimbus_rg" {
    name = var.resource_group_name
    location = var.resource_group_location
}

resource "azurerm_storage_account" "nimbus_sa" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.nimbus_rg.name
  location                 = azurerm_resource_group.nimbus_rg.location
  account_kind = "StorageV2"
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = "true"

}

resource "azurerm_storage_data_lake_gen2_filesystem" "numbus-dl" {
  name               = "nimbus-data-lake"
  storage_account_id = azurerm_storage_account.nimbus_sa.id
}

