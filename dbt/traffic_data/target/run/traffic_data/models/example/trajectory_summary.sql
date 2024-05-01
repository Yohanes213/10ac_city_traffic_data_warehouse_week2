
  create view "traffic"."traffic_schema"."trajectory_summary__dbt_tmp"
    
    
  as (
    WITH trajectory_summary AS(
    SELECT
        track_id,
        MAX(speed) As max_speed,
        MAX(lat_acc) AS max_lat_acc,
        MAX(lon_acc) AS max_lon_acc
        -- MAX(time) AS total_time
    
    FROM trajectory
    GROUP BY track_id
)

SELECT * FROM trajectory_summary
  );