-- Script to create a new user in server (DDL query)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Query to grant perms to user
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
