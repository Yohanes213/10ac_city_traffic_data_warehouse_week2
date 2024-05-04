## Traffic data warehouse

This project provides a dbt and Airflow setup for transforming traffic data and creating analytical models.


## Contents

- **dags**: Directory containing Airflow DAG script.
- **dbt**: Directory containing DBT project structure.
  - **logs**: Directory to store DBT logs.
  - **traffic_data**: DBT project directory.
    - **analysis**: Directory for DBT analysis models.
    - **macros**: Directory for DBT macros.
    - **models**: Directory for DBT models.
    - **seeds**: Directory for DBT seed data.
    - **snapshots**: Directory for DBT snapshots.
    - **tests**: Directory for DBT tests.
  - **.gitignore**: Git ignore file for DBT project.
  - **README.md**: Readme file for DBT project.
  - **dbt_project.yml**: DBT project configuration file.
- **.gitignore**: Git ignore file for the entire repository.
- **README.md**: Main Readme file for the repository.

## `airflow_dbt_executor.py`

This Python script defines an Airflow DAG (`dbt_dag`) to execute DBT commands using BashOperators.

### DAG Details:

- **DAG ID**: `dbt_dag`
- **Schedule Interval**: Daily (`@daily`)
- **Start Date**: May 1, 2024
- **Catchup**: Disabled

### Tasks:

1. **dbt_debug**: Task to run `dbt debug` command.
2. **dbt_run**: Task to run `dbt run` command.

The `dbt_debug` task is followed by the `dbt_run` task.

Both tasks are configured to retry on failure with a delay of 5 minutes, and `dbt_run` is configured to retry up to 3 times.

## Instructions

To use this DAG:

1. Clone this repository.
2. Place the `airflow_dbt_executor.py` file in your Airflow DAGs folder.
3. Ensure DBT is installed in your Airflow environment.
4. Adjust the paths and commands in the DAG script (`airflow_dbt_executor.py`) as needed.
5. Trigger the DAG in Airflow to execute DBT commands according to the defined schedule.
