-- script that creates the table unique_id
-- description id, name
-- id int should have default 1 and unique
-- script should not fail if table already exists
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
