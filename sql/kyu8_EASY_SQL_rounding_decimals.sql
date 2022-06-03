-- Given the following table 'decimals':
--
-- https://www.codewars.com/kata/594a6133704e4daf5d00003d
--
-- decimals table schema
--
--     id
--     number1
--     number2
--
-- Return a table with two columns (number1, number2) where the
-- values in number1 have been rounded down and the values in number2
-- have been rounded up

SELECT FLOOR(number1) AS number1, CEILING(number2) AS number2 FROM decimals;