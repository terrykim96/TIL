CREATE TABLE countries(
  id INTEGER PRIMARY KEY,
  room_num TEXT not NULL,
  check_in TEXT not NULL,
  check_out TEXT not NULL,
  grade TEXT not NULL,
  price INTEGER not NULL
);

INSERT INTO countries(room_num, check_in, check_out, grade, price)
VALUES('B203', '2019-12-31', '2020-01-03', 'suite', '900'),
('1102', '2020-01-04', '2020-01-08', 'suite', '850'),
('303', '2020-01-01', '2020-01-03', 'deluxe', '500'),
('807', '2020-01-04', '2020-01-07', 'superior', '300');

ALTER TABLE countries
RENAME TO hotels;

SELECT *
FROM hotels
ORDER BY grade DESC;

SELECT *
FROM hotels
WHERE room_num LIKE 'B%' or grade='deluxe';

SELECT *
FROM hotels
WHERE check_in='2020-01-04' and room_num NOT LIKE 'B%'
ORDER BY price ASC;