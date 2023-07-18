-- script that creates a table called first_table in database
-- should contain id INT, name VARCHAR(256)
-- script should not fail if table already exists
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
)
