from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

with DAG(
    dag_id="dbt_dag",
    schedule_interval="@daily", 
    start_date=datetime(2024, 5, 1), 
    catchup=False  
) as dag:

    dbt_debug = BashOperator(
        task_id="dbt_debug",
        bash_command="dbt debug",
        retries=1,  
        retry_delay=timedelta(minutes=5),
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="dbt run",
        retries=3,
        retry_delay=timedelta(minutes=5),
    )

    dbt_debug >> dbt_run  

