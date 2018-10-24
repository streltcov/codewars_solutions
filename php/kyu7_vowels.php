<?php

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

echo getCount('ababababa');
