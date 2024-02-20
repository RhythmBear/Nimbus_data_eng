from airflow import DAG
from airflow.providers.microsoft.azure.hooks.wasb import WasbHook
from dotenv import load_dotenv
import os


load_dotenv()


def upload_file_to_data_lake(
        container_name,
        file_path,
):
    
    blob_name = file_path.split('/')[-1]
    blob_name = blob_name.replace(' ', '_')
    
    print(f"Uploading {blob_name} to {container_name}")
    az_hook = WasbHook(wasb_conn_id='nimbus-container')
    az_hook.load_file(
        file_path=file_path,
        container_name=container_name,
        blob_name=blob_name

    )
    

    