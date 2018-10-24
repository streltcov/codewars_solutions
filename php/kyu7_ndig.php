<?php

function nbDig($n, $d) {
    $count = 0;
    $square = '';
    $d = (string)$d;

    while ($n >= 0) {
        $square = $square.(string)($n ** 2);
        $n--;
    }

    $square = str_split($square);

    foreach ($square as $l) {
        if (preg_match("/$d/", $l)) {
            $count++;
        }
    }

    return $count;
}

echo nbDig(5750, 0).PHP_EOL;
