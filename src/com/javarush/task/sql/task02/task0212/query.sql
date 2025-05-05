-- Write your code here:
SELECT IF(city == 'London', IF(position == 'manager' && salary > 10000), 'good', 'bad') FROM employee