-- the statements that I run here will be stored in the git repo

-- creating the table that will contain the information about students
CREATE TABLE students(
  id INT, -- e.g. 0105123
  name VARCHAR(100),
  last_name VARCHAR(100),
  date_of_birth DATE, -- e.g. 1989-07-27
  favorite_number INT, -- e.g. -1.5
  country_of_origin CHAR(3), -- e.g. MEX, USA, CAN
  active TINYINT
);

SELECT * FROM students;

INSERT INTO students (id, name, last_name, date_of_birth, favorite_number, country_of_origin, active)
VALUES (0105123, 'Santiago', 'Arizti', '1989-07-27', -1.5, 'MEX', 1),
       (0105123, 'Andrea', 'Perez', '1995-01-01', 8, 'USA', 1);

SELECT date_of_birth, name FROM students ORDER BY date_of_birth DESC;

SELECT group_concat(name) FROM students;

SELECT min(date_of_birth), name FROM students;