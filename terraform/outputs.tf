output "storage_acount_connection_string" {
    value = azurerm_storage_account.nimbus_sa.primary_connection_string
    sensitive = true
}
