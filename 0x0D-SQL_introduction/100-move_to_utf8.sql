-- script that converts hbtn_0c_0 database to UTF8 in MySQL server
-- convert first_table, name, hbtn_0c_0
USE hbtn_0c_0
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
