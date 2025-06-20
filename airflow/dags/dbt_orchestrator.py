import sys
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta
from docker.types import Mount

default_args= {
    'description':'A dag to orchestrate data',
    'start_date':datetime(2025,6,17),
    'catchup':False, 
}

dag = DAG(
    dag_id='weather-dbt-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    
    task2= DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(source='/home/vxr/repos/Weather Analytics Pipeline/dbt/my_project',
                target='/usr/app',
                type='bind'),
            Mount(source='/home/vxr/repos/Weather Analytics Pipeline/dbt/profiles.yml',
                target='/root/.dbt/profiles.yml',
                type='bind'),
        ],
        network_mode='my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success',
    )
