<?php

function findShort($str){
    $str = explode(" ", $str);
    $check = count(str_split($str[0]));
    foreach ($str as $word) {
        if (count(str_split($word)) < $check) {
            $check = count(str_split($word));
        }
    }
    return $check;
}

$str1 = "bitcoin take over the world maybe who knows perhaps";

findShort($str1);
