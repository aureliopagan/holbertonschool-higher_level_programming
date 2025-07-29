-- Count the number of TV shows in each genre and sort by the count in descending order
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id  -- Join genres with shows
GROUP BY tv_genres.name  -- Group results by genre name
HAVING COUNT(tv_show_genres.show_id) > 0  -- Filter out genres with no shows
ORDER BY number_of_shows DESC;  -- Sort by the number of shows in descending order
