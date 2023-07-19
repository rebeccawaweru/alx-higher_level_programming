-- script that creates database hbtn_0d_usa & table cities
-- cities description id, state_id and name
-- id INT, unique, auto generated can't be null, primary key
-- state_id INT, can't be null,FOREIGN KEY
-- name VARCHAR, can't be null
-- script should not fail if database or cities exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
