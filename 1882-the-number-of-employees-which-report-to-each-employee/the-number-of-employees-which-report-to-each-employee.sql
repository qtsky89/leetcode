-- Write your PostgreSQL query statement below

WITH Manager AS (SELECT reports_to AS manager_id, COUNT(*) AS reports_count, ROUND(AVG(age), 0) AS average_age FROM Employees
WHERE reports_to IS NOT NULL
GROUP BY reports_to)

SELECT e.employee_id, e.name, m.reports_count, m.average_age FROM Employees e
INNER JOIN Manager m ON e.employee_id = m.manager_id
ORDER BY employee_id