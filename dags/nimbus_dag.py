from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.microsoft.azure.hooks.wasb import WasbHook
from airflow.providers.microsoft.azure.transfers.local_to_adls import LocalFilesystemToADLSOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from tempfile import NamedTemporaryFile
from include.utils import upload_file_to_data_lake
import os

default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}

local_path_og = r"files/OWNERSHIP OG DATA.csv"
local_path_updated = r"files/OWNERSHIP UPDATED DATA.csv"

with DAG(
    dag_id='connect_load_data_etl',
    description='Dag to transform and process Nimbus Maps Assignment.',
    default_args=default_args,
    start_date=datetime(2023, 2, 2),
    schedule_interval='@once',
    tags=['complete_etl']
) as dag:
    
    start_workflow = DummyOperator(task_id='start_workflow')

    upload_og_file = PythonOperator(
        task_id = 'upload_og_file',
        python_callable=upload_file_to_data_lake,
        op_kwargs={
            'container_name': 'nimbus-data-lake/inputs',
            'file_path': local_path_og
        }
    )
    upload_updated_file = PythonOperator(
        task_id = 'upload_updated_file',
        python_callable=upload_file_to_data_lake,
        op_kwargs={
            'container_name': 'nimbus-data-lake/inputs',
            'file_path': local_path_updated
        }
    )
    
    

    end_workflow = DummyOperator(task_id='end_workflow')


    start_workflow >> upload_og_file >> upload_updated_file >> end_workflow

    dag.doc_md = __doc__