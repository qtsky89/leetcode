-- Write your PostgreSQL query statement below

/*
    2019-06-25 -> 2019-07-20 -> 2019-07-21 
    

*/

SELECT activity_date AS day, COUNT(DISTINCT(user_id)) AS active_users FROM Activity
WHERE activity_date > '2019-06-27' AND activity_date <= '2019-07-27'
GROUP BY day
ORDER BY day ASC