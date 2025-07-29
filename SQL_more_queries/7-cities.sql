-- Create the database only if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the newly created database
USE hbtn_0d_usa;

-- Create the table only if it isn't already present
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,  -- Auto-incrementing unique ID, primary key
    state_id INT NOT NULL,                              -- State ID, mandatory field
    name VARCHAR(256) NOT NULL,                         -- City name, mandatory and limited to 256 characters
    -- Foreign key linking state_id to the id column in the states table
    FOREIGN KEY (state_id) REFERENCES states(id)
);
