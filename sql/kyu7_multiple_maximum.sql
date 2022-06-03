-- Maximum multiple;
--
-- https://www.codewars.com/kata/5aba780a6a176b029800041c
--
-- Given a Divisor and a Bound, Find the largest integer N, Such That:
--
-- Conditions :
--      N is divisible by divisor
--      N is less than or equal to bound
--      N is greater than 0

SELECT divisor * (bound/divisor) AS res FROM max_multiple;