<?php

/**
 * Return the number (count) of vowels in the given string
 * We will consider a, e, i, o, and u as vowels for this Kata
 * The input string will only consist of lower case letters and/or spaces
 */

/**
 * solution
 */

function getCount($str) {
    $vowelsCount = 0;
    $str = str_split($str);

    $vowels = ['a', 'e', 'i', 'o', 'u'];
    foreach ($vowels as $vowel) {
        foreach ($str as $letter) {
            if ($vowel == $letter) {
                $vowelsCount++;
            }
        }
    }

    return $vowelsCount;
  }
