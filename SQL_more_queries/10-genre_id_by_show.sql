-- Retrieve all TV shows that have at least one genre associated with them
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id  -- Join shows with their genres
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;  -- Sort by show title and genre ID in ascending order
