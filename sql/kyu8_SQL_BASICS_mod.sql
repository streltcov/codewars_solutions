-- Mod;
--
-- https://www.codewars.com/kata/594a9592704e4d21bc000131
--
-- Given the following table 'decimals':
-- https://www.codewars.com/kata/594a9592704e4d21bc000131/train/sql
--
-- decimals table schema
--     id
--     number1
--     number2
--
-- Return a table with one column (mod) which is the
-- output of number1 modulus number2

SELECT mod(number1, number2) AS mod FROM decimals;