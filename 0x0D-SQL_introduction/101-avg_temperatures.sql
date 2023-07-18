-- script that displays the average temperature by city 
-- order by temperature Desc
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
