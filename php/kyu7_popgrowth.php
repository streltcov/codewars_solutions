<?php

function nbYear($p0, $percent, $aug, $p) {
    // your code
    $year = function($p0, $percent, $aug, $acc) use(&$year, &$p) {
      if ($p0 >= $p) {
        return $acc;
      } else {
        return $year(($p0 + $p0 * ($percent / 100) + $aug), $percent, $aug, ($acc + 1));
      }
    };
    return $year($p0, $percent, $aug, 0);
}

$a = nbYear(1500, 5, 100, 5000);

echo $a.PHP_EOL;
