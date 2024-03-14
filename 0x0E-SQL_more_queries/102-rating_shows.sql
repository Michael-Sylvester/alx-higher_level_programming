-- List all shows with rating

SELECT title, SUM(rate) as rating
FROM tv_shows, tv_show_ratings
WHERE tv_shows.id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating DESC;