-- Ensure the table is created only if it doesn't already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,                      -- Unique identifier for each entry
    name VARCHAR(256) NOT NULL   -- Name field, mandatory and limited to 256 characters
);
