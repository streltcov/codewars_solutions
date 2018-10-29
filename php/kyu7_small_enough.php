<?php

/**
 * You will be given an array and a limit value. You must check that all values in the
 * array are below or equal to the limit value. If they are, return true. Else, return false
 * 
 * You can assume all values in the array are numbers
 */

/**
 * solution
 */

function smallEnough($a, $limit)
{
    $result = true;
    array_map(function($item) use(&$result, $limit) {
        if ($item > $limit) {
            $result = false;
        }
    }, $a);

    return $result;
}
