-- Write your PostgreSQL query statement below

WITH distinct_customer AS (SELECT DISTINCT visited_on FROM Customer)

SELECT c1.visited_on, SUM(c2.amount) AS amount, ROUND(SUM(c2.amount)::numeric / 7, 2) AS average_amount FROM distinct_customer c1
INNER JOIN Customer c2 ON (c1.visited_on - c2.visited_on) >= 0 AND (c1.visited_on - c2.visited_on) <= 6
GROUP BY c1.visited_on
HAVING COUNT(DISTINCT c2.visited_on) >= 7
ORDER BY c1.visited_on ASC