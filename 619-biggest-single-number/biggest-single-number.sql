-- Write your PostgreSQL query statement below

WITH unique_num AS 
(SELECT num, COUNT(*) FROM MyNumbers
GROUP BY num
HAVING COUNT(*) = 1
)

SELECT MAX(num) AS num FROM unique_num