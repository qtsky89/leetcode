-- Write your PostgreSQL query statement below

WITH total_count AS (SELECT COUNT(*) AS total_count FROM Seat)

SELECT 
    (CASE
        WHEN id % 2 != 0 AND total_count != id THEN id + 1
        WHEN id % 2 != 0 AND total_count = id THEN id
        ELSE id - 1
    END) AS id, student
FROM Seat, total_count
ORDER BY id ASC