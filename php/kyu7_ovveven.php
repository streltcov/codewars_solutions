<?php

function odd_or_even(array $a): string {
    $a = array_sum($a);
    if ($a % 2 == 0) {
        return 'even';
    } else {
        return 'odd';
    }
}
