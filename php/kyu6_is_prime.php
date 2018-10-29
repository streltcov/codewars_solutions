<?php

/**
 * Is Prime
 * Define a function isPrime/is_prime() that takes one integer argument and returns true/True
 * or false/False depending on if the integer is a prime
 * 
 * Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive
 * divisors other than 1 and itself
 * 
 * Example
 * bool isPrime(5) = return true
 * 
 * Assumptions
 *     You can assume you will be given an integer input
 *     You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0)
 */

/**
 * solution
 */

function is_prime(int $n): bool {
    if($n <= 1) return false;
    if($n == 2) return true;
    if($n % 2 == 0) return false;
    $a = intval(sqrt($n));
    echo $a;
    $i = 3;
    while($i <= $a) {
         if($n % $i == 0) return false;
         $i+=2;
    }
    return true;
}
