-- Create the table only if it isn't already present
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,     -- Unique identifier with a default value of 1
    name VARCHAR(256)            -- Name field, can store up to 256 characters
);
