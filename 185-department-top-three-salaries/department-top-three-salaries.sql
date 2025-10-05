-- Write your PostgreSQL query statement below

-- SELECT d.name AS "Department", e.name AS "Employee", e.salary AS "Salary" FROM (SELECT 
--     departmentId, 
--     name, 
--     salary,
--     DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rank
-- FROM Employee) e
-- INNER JOIN Department d ON e.departmentId = d.id
-- WHERE e.rank <= 3
-- ORDER BY e.rank DESC


SELECT d.name AS "Department", e.name AS "Employee", e.salary AS "Salary"
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e.departmentId AND e2.salary >= e.salary
) <= 3