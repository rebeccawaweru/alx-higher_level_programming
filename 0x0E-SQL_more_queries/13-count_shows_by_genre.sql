-- script to lists genres using given criteria
SELECT tv_genres.name AS genre, COUNT(*) AS 'number_shows'
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_shows DESC;
