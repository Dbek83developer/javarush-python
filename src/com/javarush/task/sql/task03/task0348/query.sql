-- Write your code here:
WITH grossed_total AS
         (SELECT SUM(grossed) AS total
          FROM films)
SELECT AVG(total) average_grossed
FROM grossed_total;