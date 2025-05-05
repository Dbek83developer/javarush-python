-- Write your code here:
SELECT department as department_name,
COUNT(*) as count
FROM employee
WHERE position = 'frontend developer' OR position = 'backend developer'
GROUP BY department