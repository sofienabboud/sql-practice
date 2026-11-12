
--an example of an sql SELECT FROM query
/*
=======================
SELECT column1, column2
FROM table_name;
=======================
*/

--practice 1
SELECT make, model, year, price
FROM vehicles;

--practice 2
SELECT make, model, price
FROM vehicles
WHERE price < 20000;

--practice 3
SELECT make, model, price, mileage
FROM vehicles
WHERE price < 25000 AND mileage < 40000;

--practice 4
SELECT make, model, year, price
FROM vehicles
WHERE make = 'Toyota' OR make = 'Honda';

--practice 5
SELECT make, model, year, price
FROM vehicles
ORDER BY price DESC;

--practice 6
SELECT make, model, year, price
FROM vehicles
ORDER BY year DESC
LIMIT 5;

--practice 7
SELECT make, model, year, price, mileage
FROM vehicles
WHERE price < 30000 AND mileage < 50000 AND year >= 2020
ORDER BY price ASC
LIMIT 3;



