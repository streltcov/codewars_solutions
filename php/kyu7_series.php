<?php

function series_sum($n) {
    $b = 4.00;
    $sum = 1;
    $i = 1;

    if ($n == 1) return $n.'.00';

    while ($i < $n) {
        $sum = $sum + 1 / $b;
        $i++;
        $b = $b + 3;
    }

    return (string)round($sum, 2);
}

echo series_sum(1).PHP_EOL;
echo series_sum(2).PHP_EOL;
echo series_sum(3).PHP_EOL;
echo series_sum(4).PHP_EOL;
