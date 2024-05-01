#from airflow import DAG
#from airflow.providers.postgres.operators.postgres import PostgresOperator

#from airflow.operators.postgres_operator import PostgresOperator

# # Replace with your connection details (assuming same connection as in previous files)
#postgres_conn_id = "postgres"

#with DAG(
 #    dag_id="trajectory_summary_dag",
#     start_date=datetime(2024, 5, 1),  # Adjust start date as needed
#     schedule_interval="@daily",
# ) as dag:

#     create_trajectory_summary_table = PostgresOperator(
#         task_id="create_trajectory_summary_table",
#         postgres_conn_id=postgres_conn_id,
#         sql="""
#           WITH trajectory_summary AS(
#               SELECT
#                   track_id,
#                   MAX(speed) As max_speed,
#                   MAX(lat_acc) AS max_lat_acc,
#                   MAX(lon_acc) AS max_lon_acc,
#                   AVG(time) AS average_time

#               FROM trajectory
#               GROUP BY track_id
#           )

#           SELECT * FROM trajectory_summary
#         """,
#     )

#     # Consider task dependencies and error handling as mentioned in vehicle_info.py
