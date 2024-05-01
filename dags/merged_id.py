# from airflow import DAG
# from airflow.operators.postgres import PostgresOperator

# # Replace with your connection details (assuming a connection named "postgres_default")
# postgres_conn_id = "postgres_default"

# with DAG(
#     dag_id="merged_id_dag",
#     start_date=datetime(2024, 5, 1),  # Adjust start date as needed
#     schedule_interval="@daily",
# ) as dag:

#     create_merged_id_table = PostgresOperator(
#         task_id="create_merged_id_table",
#         postgres_conn_id=postgres_conn_id,
#         sql="""
#           {{ config(materialized='table') }}

#           WITH merged_data AS(
#               SELECT
#                   v.track_id,
#                   v.car_type,
#                   v.traveled_d,
#                   v.avg_speed,
#                   t.max_speed,
#                   t.max_lat_acc,
#                   t.max_lon_acc,
#                   t.average_time

#               FROM vehicles AS v
#               JOIN {{ ref('trajectory_summary') }} AS t
#               ON v.track_id = t.track_id
#           )

#           SELECT * FROM merged_data
#         """,
#     )

#     # Consider adding logic to handle potential errors during table creation
#     # (e.g., using `create_if_not_exists` or similar PostgreSQL features)
