-- script that lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
SELECT cities.*,states.name FROM cities INNER JOIN states ON cities.id=states.id ORDER BY cities.id ASC;
