-- Write your PostgreSQL query statement below

SELECT 
TO_CHAR(trans_date, 'YYYY-mm') AS month,
country,
COUNT(*) AS trans_count,
SUM((state = 'approved')::int) AS approved_count,
SUM(amount) AS trans_total_amount,
SUM((state = 'approved')::int * amount) AS approved_total_amount
FROM Transactions
GROUP BY TO_CHAR(trans_date, 'YYYY-mm'), country
