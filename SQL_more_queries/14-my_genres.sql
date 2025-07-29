-- Retrieve the genres associated with the TV show "Dexter" and sort them alphabetically
SELECT tv_genres.name
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id  -- Join shows with their genres
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id  -- Join genres to get genre names
WHERE tv_shows.title = 'Dexter'  -- Filter for the show "Dexter"
ORDER BY tv_genres.name ASC;  -- Sort the genre names in ascending order
