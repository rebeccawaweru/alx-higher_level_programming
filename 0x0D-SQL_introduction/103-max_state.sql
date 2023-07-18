-- script that displays the max temperature of each state
-- order by State name
SELECT state, MAX(value) AS temp_max FROM temperatures GROUP BY state ORDER BY state ASC;
