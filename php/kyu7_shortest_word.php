<?php

/**
 * Simple, given a string of words, return the length of the shortest word(s)
 * String will never be empty and you do not need to account for different data types
 */

/**
 * solution
 */

function findShort($str){
    $str = explode(" ", $str);
    $check = count(str_split($str[0]));
    foreach ($str as $word) {
        if (count(str_split($word)) < $check) {
            $check = count(str_split($word));
        }
    }
    return $check;
}
