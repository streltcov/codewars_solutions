<?php

function repeatStr($n, $str)
{
    $add = $str;
    for($i = 1; $i < $n; $i++) {
        $str = $str.$add;
    }
    return $str;
}

echo repeatStr(9, 'l');
