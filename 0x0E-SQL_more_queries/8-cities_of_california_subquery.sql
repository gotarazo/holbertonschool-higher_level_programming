-- Lists all cities of CA in database hbtn_0d_usa ordered by ascending cities.id
SELECT id,name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
