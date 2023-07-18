-- script that lists all records of the second_table
-- don't list rows without name value
-- display score and name in this order
-- list should be in descending order of dcore
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
