## Traffic data warehouse

This project provides a dbt and Airflow setup for transforming traffic data and creating analytical models.

Project Structure:

traffic_data/
- analysis/       # (Optional) Directory for custom dbt analyses
- dbt_packages/  # Installed dbt packages
- logs/           # dbt execution logs
- macros/         # (Optional) Directory for custom dbt macros
- models/         # dbt SQL models for data transformation
   - merged_id.sql
   - trajectory_summary.sql
   - vehicle_info.sql
- seeds/          # (Optional) Directory for data seeding scripts
- snapshots/      # dbt model snapshots
- target/         # dbt-generated artifacts
- tests/          # Unit tests for dbt models (optional)
- .gitignore      # Git ignore configuration
- dbt_project.yml  # dbt project configuration file

### Requirements:

dbt: https://docs.getdbt.com/

Airflow: https://airflow.apache.org/docs/

PostgreSQL (or your target database)


### Setup:

1. Install dbt and Airflow: Follow the installation instructions for your environment.
2. Database Connection:
    - Create a file named profiles.yml in your home directory (usually ~/.dbt/).
    - Define a profile named traffic_data in profiles.yml with your actual database connection details (target, host, port, user, password, database).
3. Initialize dbt project: Navigate to the traffic_data directory and run dbt init.
4. Configure Airflow DAG (dags/bash.py): Update the DAG configuration in bash.py with your desired schedule and potentially add custom error handling functions.
5. Start Airflow Webserver: Follow the instructions for starting the Airflow webserver.

### Running the Pipeline:

The Airflow DAG (dbt_dag) is defined in dags/bash.py. It includes tasks for:
Optional dbt debug (commented out)
dbt run to execute SQL models for transformation
The DAG typically runs daily (adjust the schedule in bash.py if needed).


### dbt Models:

Traffic data models are located in the models directory.
Each model is a separate SQL file defining transformations for your traffic data.
Consider adding comments to document the purpose of each model.

### Further Development:

Add new dbt models for additional data transformations.
Create custom dbt analyses and macros in the respective directories.
Enhance the Airflow DAG with additional tasks and dependencies for a more complex workflow.
