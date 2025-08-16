-- Write your PostgreSQL query statement below

SELECT s.user_id, ROUND(COALESCE(AVG((c.action = 'confirmed')::int), 0), 2) confirmation_rate   FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id