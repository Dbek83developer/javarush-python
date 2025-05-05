-- Write your code here:
SELECT id IF(id<4 && salary>1000, 'yes', 'no') FROM employee