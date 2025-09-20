-- Write your PostgreSQL query statement below

WITH top_user AS (
    SELECT u.name AS results
    FROM MovieRating r
    INNER JOIN Users u ON r.user_id = u.user_id
    GROUP BY u.name
    ORDER BY COUNT(*) DESC, u.name ASC
    LIMIT 1
),
top_movie AS (
    SELECT m.title AS results
    FROM MovieRating r
    INNER JOIN Movies m ON r.movie_id = m.movie_id
    WHERE r.created_at >= '2020-02-01' AND r.created_at < '2020-03-01'
    GROUP BY m.title
    ORDER BY AVG(r.rating) DESC, m.title ASC
    LIMIT 1
)
SELECT * FROM top_user
UNION ALL
SELECT * FROM top_movie;