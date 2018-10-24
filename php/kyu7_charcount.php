<?php

function count_char(string $s, string $c): int {
    $count = 0;
    $s = str_split($s);
    //print_r($s);
    foreach ($s as $letter) {
        $letter = strtolower($letter);
        if ($c == $letter) {
            $count++;
        }
    }
    return $count;
}

echo count_char("Fancy fifth fly aloof", "f");
