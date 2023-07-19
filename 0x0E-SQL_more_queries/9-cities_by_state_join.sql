-- script that lists all cities contained in databse
-- use only one SELECT
-- results in ASC
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
