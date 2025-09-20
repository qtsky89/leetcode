-- Write your PostgreSQL query statement below

WITH last_person AS (SELECT q1.turn, q1.person_name, SUM(q2.weight) FROM Queue q1
INNER JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn, q1.person_name
HAVING SUM(q2.weight) <= 1000
ORDER BY q1.turn DESC
LIMIT 1)

SELECT person_name FROM last_person