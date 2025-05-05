-- Write your code here:
SELECT
CASE
    WHEN euro IS NOT NULL THEN 'bad'
    ELSE 'good'
END
FROM cars