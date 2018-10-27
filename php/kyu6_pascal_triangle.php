<?php

/**
 * Write a function that, given a depth (n), returns a single-dimensional
 * array/list representing Pascal's Triangle to the n-th level
 * For example:
 * pascals_triangle(4) == [1,1,1,1,2,1,1,3,3,1]
 */

/**
 * solution
 */

function pascals_triangle($n) {
    $rows = [];

    $generate_row = function ($number) {
        $currentRow = [1];
        for ($i = 0; $i < $number; $i++) {
            $newRow = [];
            for ($j = 0; $j <= $number; $j++) {
                $first = isset($currentRow[$j - 1]) ? $currentRow[$j - 1] : 0;
                $second = isset($currentRow[$j]) ? $currentRow[$j] : 0;
                $newRow[$j] = $first + $second;
            }
            $currentRow = $newRow;
        }
        return $currentRow;
    };

    for($i = 0; $i < $n; $i++) {
             $rows = array_merge($rows, $generate_row($i));
    }

    return $rows;
}
