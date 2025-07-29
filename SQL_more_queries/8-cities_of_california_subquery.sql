-- Retrieve all cities located in California
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')  -- Get the state ID for California
ORDER BY id ASC;  -- Sort the results by city ID in ascending order
