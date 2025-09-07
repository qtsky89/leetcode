-- Write your PostgreSQL query statement below

-- step1. make sub query to check how many empoyee_id : department_id count is
WITH Department AS (SELECT employee_id, COUNT(*) AS department_count FROM Employee
GROUP BY employee_id)

-- step2. Used where condition
SELECT e.employee_id, e.department_id FROM Employee e
INNER JOIN Department d ON e.employee_id = d.employee_id
WHERE d.department_count = 1 OR e.primary_flag = 'Y'