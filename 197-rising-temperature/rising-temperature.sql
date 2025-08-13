-- Write your PostgreSQL query statement below

SELECT C.id FROM Weather AS C
INNER JOIN Weather AS P ON C.recordDate = P.recordDate + INTERVAL '1 day'
WHERE C.temperature > P.temperature