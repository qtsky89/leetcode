-- Write your PostgreSQL query statement below
WITH product_count AS (SELECT COUNT(*) AS count FROM Product)

SELECT customer_id FROM Customer
CROSS JOIN product_count
GROUP BY customer_id, product_count.count
HAVING COUNT(DISTINCT(product_key)) = product_count.count