

WITH merged_data AS(
    SELECT 
    v.track_id,
    v.car_type,
    v.traveled_d,
    v.avg_speed,
    t.max_speed,
    t.max_lat_acc,
    t.max_lon_acc,
    t.average_time
    
    FROM vehicles AS v
    JOIN "traffic"."traffic_schema"."trajectory_summary" AS t
    ON v.track_id = t.track_id
)

SELECT * FROM merged_data