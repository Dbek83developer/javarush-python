-- Write your code here:
SELECT YEAR(prod_date) as prod_year, MONTH(prod_date) as prod_month, COUNT(*)
FROM cars
GROUP BY prod_year, prod_month
