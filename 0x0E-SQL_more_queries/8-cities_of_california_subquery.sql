-- Set the database name
USE hbtn_0d_usa;

-- List all cities of California
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
