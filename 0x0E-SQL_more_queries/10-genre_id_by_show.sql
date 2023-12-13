-- List all shows with at least one linked genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE EXISTS (
    SELECT 1
    FROM tv_show_genres
    WHERE tv_show_genres.show_id = tv_shows.id
)
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
