-- Write your code here:
SELECT IF(age <= 12, 'child', IF(age <20), 'teenager', 'adult') FROM customers LIMIT 5