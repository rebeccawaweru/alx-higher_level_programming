-- list all the cities of California
-- result must be in ascending order
-- don't use JOIN
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
GROUP BY id
ORDER BY id ASC;
