-- Retrieve the titles of TV shows that belong to the "Comedy" genre and sort them alphabetically
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id  -- Join shows with their genres
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id  -- Join genres to get genre names
WHERE tv_genres.name = 'Comedy'  -- Filter for shows in the "Comedy" genre
ORDER BY tv_shows.title ASC;  -- Sort the show titles in ascending order
