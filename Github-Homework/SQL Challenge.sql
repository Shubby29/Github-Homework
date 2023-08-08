DROP DATABASE IF EXISTS foundation_assessment_ii;
CREATE DATABASE foundation_assessment_ii;
USE foundation_assessment_ii;

-- create movie_info table in DB
CREATE TABLE movie_info(
`movie_ID` INT NOT NULL,
`movie_Name` VARCHAR (50) NOT NULL,
`movie_Length` TIME,
`age_rating` VARCHAR (50) NOT NULL,
PRIMARY KEY (`movie_ID`)
);

CREATE TABLE screens(
`screen_ID` INT NOT NULL,
`four_K` BOOLEAN,
PRIMARY KEY (`screen_ID`)
);

CREATE TABLE showings(
  `showing_ID` INT NOT NULL,
  `movie_ID` INT NOT NULL,
  `screen_ID` INT NOT NULL,
  `start_time` DATETIME,
  `available_seats` INT NOT NULL,
  PRIMARY KEY (`showing_ID`)
);

 INSERT INTO movie_info(movie_ID, movie_name, movie_length, age_rating)
 VALUES 
 (1, 'The Movie', '02:19:00', '12A'),
 (2, 'The Other Movie', '01:30:00', '15'),
 (3, 'The 3D Amazing Movie', '01:42:00', 'PG'),
 (4, 'La Allure', '01:09:00', '18'),
 (5, 'The Cartoon', '01:15:00', 'U'),
 (6, 'The Scary Cartoon', '01:23:00', 'PG'),
 (7, 'The Coming Of Age', '01:40:00', '12A'),
 (8, 'The War', '02:07:00', '15'),
 (9, 'The Murder Mystery', '01:47:00', '15');

 INSERT INTO screens(screen_ID, four_k)
 VALUES 
  (1, True),
  (2, False),
  (3, True),
  (4, True),
  (5, True),
  (6, True),
  (7, True),
  (8, False),
  (9, True),
  (10, True);
INSERT INTO showings(showing_ID, movie_ID, screen_ID, start_time, available_seats)
VALUES 
  (1, 1, 2, CAST('2023-01-01 12:00:01' AS DATETIME), 10),
  (2, 1, 2, CAST('2023-01-01 17:00:00' AS DATETIME), 23),
  (3, 2, 9, CAST('2023-01-01 10:30:00' AS DATETIME), 30),
  (4, 3, 1, CAST('2023-01-01 07:00:00' AS DATETIME), 38),
  (5, 3, 5, CAST('2023-01-01 10:00:00' AS DATETIME), 26),
  (6, 3, 1, CAST('2023-01-01 17:00:00' AS DATETIME), 5),
  (7, 3, 1, CAST('2023-01-01 19:00:00' AS DATETIME), 0),
  (8, 3, 5, CAST('2023-01-01 14:00:00' AS DATETIME), 2),
  (9, 4, 9, CAST('2023-07-11 20:00:00' AS DATETIME), 14),
  (10, 4, 9, CAST('2023-07-11 23:00:00' AS DATETIME), 23),
  (11, 5, 6, CAST('2023-01-01 09:30:00' AS DATETIME), 30),
  (12, 5, 6, CAST('2023-07-11 12:30:00' AS DATETIME), 7),
  (13, 5, 6, CAST('2023-07-11 14:30:00' AS DATETIME), 0),
  (14, 5, 6, CAST('2023-07-11 15:20:00' AS DATETIME), 0),
  (15, 6, 10, CAST('2023-07-11 10:00:00' AS DATETIME), 32),
  (16, 6, 10, CAST('2023-07-11 13:30:00' AS DATETIME), 25),
  (17, 6, 10, CAST('2023-07-11 17:00:00' AS DATETIME), 14),
  (18, 7, 7, CAST('2023-07-11 2023-07-11 12:00:00' AS DATETIME), 36),
  (19, 8, 4, CAST('2023-07-11 15:00:00' AS DATETIME), 24),
  (20, 9, 3, CAST('2023-07-11 17:00:00' AS DATETIME), 0);
SELECT * FROM movie_info;
SELECT * FROM screens;
SELECT * FROM showings;


-- Write a query to return the name and time of all movies that play after
-- 12:00 given there is at least 1 available seat. Display the results in time
-- order.

SELECT movie_Name, start_time
FROM movie_info
JOIN showings ON movie_info.movie_ID = showings.movie_ID
WHERE start_time > '12:00:00' AND available_seats > 0
ORDER BY start_time;


4.2
SELECT movie_name 
FROM movie_info
WHERE movie_ID(
SELECT movie_ID
FROM showings
GROUP BY movie_ID
ORDER BY COUNT(*) DESC
LIMIT 1

);

