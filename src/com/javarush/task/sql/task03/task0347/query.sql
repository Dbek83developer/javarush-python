-- Write your code here:
SELECT *
FROM film_directors
         RIGHT JOIN (SELECT title, director_id FROM films WHERE films.year_released > 1990) AS film
                    ON film.director_id = film_directors.id
WHERE film_directors.country = 'USA' LIMIT 5
