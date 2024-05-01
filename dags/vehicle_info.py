# from airflow import DAG
# from airflow.providers.postgres.operators.postgres import PostgresOperator

# # Replace with your connection details (assuming same connection as in merged_id.py)
# postgres_conn_id = "postgres_default"

# with DAG(
#     dag_id="vehicle_info_dag",
#     start_date=datetime(2024, 5, 1),  # Adjust start date as needed
#     schedule_interval="@daily",
# ) as dag:

#     create_vehicle_info_table = PostgresOperator(
#         task_id="create_vehicle_info_table",
#         postgres_conn_id=postgres_conn_id,
#         sql="""
#           {{ config(materialized='table') }}

#           WITH vehicle_info AS(
#               SELECT
#                   car_type AS "vehicle_type",
#                   COUNT(car_type) AS "vehicle_count",
#                   -- AVG(speed) AS "average_speed",
#                   ROUND(AVG(CAST(traveled_d AS NUMERIC)), 2) AS "Average traveled distance",
#                   ROUND(AVG(CAST(avg_speed AS NUMERIC)), 2) AS "Avergae speed by vehicle",
#                   ROUND(AVG(CAST(average_time AS NUMERIC)), 2) AS "Avergae time by vehicle"

#               FROM {{ ref('merged_id') }}
#               GROUP BY car_type
#           )

#           SELECT * FROM vehicle_info
#         """,
#     )

#     # Consider adding task dependencies (if one DAG relies on another's output)
#     # create_merged_id_table >> create_vehicle_info_table  # Example dependency

#     # Consider error handling for table creation or data retrieval
