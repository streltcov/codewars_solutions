<?php

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

echo find_uniq([0, 1, 0]);
