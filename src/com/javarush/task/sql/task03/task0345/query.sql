-- Write your code here:
SELECT last_name FROM film_directors
         LEFT JOIN (SELECT grossed, director_id FROM films WHERE films.grossed > 100) AS film ON film.director_id = film_directors.id
WHERE film_directors.country = 'UK'
