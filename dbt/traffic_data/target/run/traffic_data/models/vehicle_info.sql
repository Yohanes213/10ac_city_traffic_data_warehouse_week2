
  
    

  create  table "traffic"."traffic_schema"."vehicle_info__dbt_tmp"
  
  
    as
  
  (
    

WITH vehicle_info AS(
    SELECT
    car_type AS "vehicle_type",
    COUNT(car_type) AS "vehicle_count",
    -- AVG(speed) AS "average_speed",
    ROUND(AVG(CAST(traveled_d AS NUMERIC)), 2) AS "Average traveled distance",
    ROUND(AVG(CAST(avg_speed AS NUMERIC)), 2) AS "Avergae speed by vehicle",
    ROUND(AVG(CAST(average_time AS NUMERIC)), 2) AS "Avergae time by vehicle"

    FROM "traffic"."traffic_schema"."merged_id"
    GROUP BY car_type
)

SELECT * FROM vehicle_info
  );
  