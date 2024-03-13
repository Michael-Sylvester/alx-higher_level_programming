-- Sleect based on 3 tables

SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL') AS genre_id
FROM tv_shows
left JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id 
WHERE tv_show_genres.genre_id IS NULL 
ORDER BY tv_shows.title, tv_show_genres.genre_id;
