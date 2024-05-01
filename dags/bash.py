from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Replace with your DAG ID and preferred schedule
with DAG(
    dag_id="dbt_dag",
    schedule_interval="@daily",  # Adjust as needed
    start_date=datetime(2024, 5, 1),  # Adjust start date if needed
    catchup=False  # Avoids rerunning for missed intervals (optional)
) as dag:

    # Optional dbt debug task for interactive testing
    dbt_debug = BashOperator(
        task_id="dbt_debug",
        bash_command="dbt debug",
        retries=1,  # Retry up to 3 times on failure
        retry_delay=timedelta(minutes=5),  # Wait 5 minutes between retries
        #on_failure_callback=SOME_ERROR_HANDLING_FUNCTION  # Custom function for handling failures (optional)
    )

    # Core dbt run task
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="dbt run",
        retries=3,
        retry_delay=timedelta(minutes=5),
        #on_failure_callback=SOME_ERROR_HANDLING_FUNCTION  # Custom function for handling failures (optional)
    )

    # Set up task dependencies (dbt_debug can run before or independently of dbt_run)
    dbt_debug >> dbt_run  # Uncomment for dbt_debug to run before dbt_run

    # Define your custom error handling function (replace with actual implementation)
