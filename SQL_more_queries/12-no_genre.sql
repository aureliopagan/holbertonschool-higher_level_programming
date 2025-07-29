-- Retrieve TV shows that do not have any genre assigned
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id  -- Join shows with genres (if any)
WHERE tv_show_genres.genre_id IS NULL  -- Filter for shows without a genre
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;  -- Sort by show title and genre ID in ascending order
