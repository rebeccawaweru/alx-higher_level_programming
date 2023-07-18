-- script that lists all records with a score >= 10 in second_table
-- list is in descending order
SELECT score, name
from second_table
WHERE score >= 10
ORDER BY score DESC
