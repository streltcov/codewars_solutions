<?php

/**
 * There is an array with some numbers. All numbers are equal except for one. Try to find it!
 * findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
 * findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
 * 
 * It’s guaranteed that array contains more than 3 numbers
 * The tests contain some very huge arrays, so think about performance
 */

/**
 * solution
 */

function find_uniq($a) {
    $check = $a[0];
    if ($check == $a[1]) {
        foreach ($a as $value) {
            if ($check != $value) return $value;
        }
    }
    if ($check == $a[2]) {
        return $a[1];
    } else {
        return $check;
    }
}
