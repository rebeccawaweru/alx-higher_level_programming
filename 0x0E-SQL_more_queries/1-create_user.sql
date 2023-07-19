-- script that creates the MySQL server user user_0d_1
-- user should have all privileges
-- set password to user_0d_1_pwd
-- script should not fail if user exists
CREATE  USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
