-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the newly created database
USE hbtn_0d_usa;

-- Create the table only if it isn't already present
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,  -- Auto-incrementing unique ID, primary key
    name VARCHAR(256) NOT NULL                          -- Name field, mandatory and limited to 256 characters
);
