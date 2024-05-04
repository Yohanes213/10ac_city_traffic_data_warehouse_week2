"""
DBT DAG: A Directed Acyclic Graph (DAG) for running dbt (data build tool) tasks.

This DAG automates the execution of dbt tasks for processing traffic data.

Tasks:
1. dbt_debug: Command to run 'dbt debug' for debug checks on the dbt project.
2. dbt_run: Command to execute 'dbt run' for processing data in the dbt project.

"""

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Define DAG
dag = DAG(
    dag_id="dbt_dag",
    schedule_interval="@daily",
    start_date=datetime(2024, 5, 1),
    catchup=False,
    default_args={
        "owner": "Airflow",
        "depends_on_past": False,
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 3,
        "retry_delay": timedelta(minutes=5),
    },
)

# Define tasks
dbt_debug = BashOperator(
    task_id="dbt_debug",
    bash_command="dbt debug",
    cwd="dbt/traffic_data",
    dag=dag,
)

dbt_run = BashOperator(
    task_id="dbt_run",
    bash_command="dbt run",
    cwd="dbt/traffic_data",
    dag=dag,
)

# Set task dependencies
dbt_debug >> dbt_run
