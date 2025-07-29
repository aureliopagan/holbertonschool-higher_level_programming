-- Create the hbtn_0d_2 database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user_0d_2 user if it doesn't already exist and set the password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant the SELECT privilege on the hbtn_0d_2 database to the user_0d_2 user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Ensure the privilege changes take effect immediately
FLUSH PRIVILEGES;

-- This script creates the database, user, and grants read-only access
