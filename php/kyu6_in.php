<?php

function inArray($array1, $array2) {
    foreach($array2 as $str2) {
        $str2 = ''.$str2;
        foreach ($array1 as $str1) {
            $str1 = ''.$str1;
            if (strpos($str2, $str1)) {
                $in[] = $str1;
            } else {
                //echo $str1."!=".$str2.PHP_EOL;
            }
        }
    }
    
    $in = array_unique($in);
    sort($in);

    print_r($in);

    return $in;
}
