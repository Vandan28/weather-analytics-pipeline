import sys
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta

# shelf no - sys.path.append, to find the main recipie that came through portal b, 
# this is the main recipie sheet , there is suplimentarty recipie sheet which has main function
# so the chef python interpretor in container will see this main recipe and look at shelf no where the supp recipe is
# this line here says this supplimentary recipie is at this location/shelf no
# so container also looks for this location to find the import 
sys.path.append('/opt/airflow/api_request') 
# where to find this insert_records recipie for main, it looks for the orchestratorpy it does not have here 
# it looks for external file locations or path that we provided above, we saying look for above path for this import 
from insert_records import main 

default_args= {
    'description':'A dag to orchestrate data',
    'start_date':datetime(2025,6,17),
    'catchup':False, 
}

dag = DAG(
    dag_id='weather-api-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    task1= PythonOperator(
        task_id='insert_records',
        python_callable= main,
    )