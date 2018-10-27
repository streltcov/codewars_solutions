<?php

/**
 * Write a function called repeatStr which repeats the given string string exactly n times
 */

/**
 * solution
 */

function repeatStr($n, $str)
{
    $add = $str;
    for($i = 1; $i < $n; $i++) {
        $str = $str.$add;
    }
    return $str;
}
