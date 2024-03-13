-- TV_shows, genres and show_enres tables SELECT

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres, tv_genres
WHERE tv_shows.id = tv_show_genres.show_id
AND tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
