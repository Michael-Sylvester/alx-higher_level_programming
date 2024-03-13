-- Count nuber of duplicates
SELECT score, COUNT(*) AS number
FROM second_table
WHERE score LIKE score
GROUP BY score
ORDER BY number DESC;
