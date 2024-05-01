# from airflow import DAG
# from airflow.operators.python import PythonOperator
# import subprocess

# def run_dbt_models(**kwargs):
#     # Call dbt run command using subprocess
#     subprocess.run(["dbt", "run"])

# # Define DAG with custom PythonOperator
# with DAG(dag_id="traffic_data_dag") as dag:

#     run_dbt_models_task = PythonOperator(
#         task_id="run_dbt_models",
#         python_callable=run_dbt_models,
#     )