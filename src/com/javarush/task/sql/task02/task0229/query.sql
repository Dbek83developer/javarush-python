-- Write your code here:
SELECT name as car_name, COUNT(*) as car_count
FROM cars
GROUP BY name