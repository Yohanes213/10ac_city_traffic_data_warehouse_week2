

WITH vehicle_summary AS (
    SELECT
    car_type AS "Vehicle type",
    COUNT(car_type) AS "Vehicle count",
    ROUND(AVG(CAST(traveled_d AS NUMERIC)), 2) AS "Average traveled distance",
    ROUND(AVG(CAST(avg_speed AS NUMERIC)), 2) AS "Avergae speed by vehicle"
    FROM Vehicles
    GROUP BY car_type 
    ORDER BY "Vehicle count" ASC
)

SELECT * FROM vehicle_summary