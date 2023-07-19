-- script that creates table id_not_null
-- description id, name
-- id INT should have default value 1
-- script should not fail if table already exists
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
