-- Retrieve all cities along with their corresponding state names
SELECT cities.id, cities.name, states.name
FROM cities
    INNER JOIN states ON cities.state_id = states.id  -- Join cities with states based on state_id
ORDER BY cities.id ASC;  -- Sort the results by city ID in ascending order
