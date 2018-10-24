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

//$a2 = ["lively", "alive", "harp", "sharp", "armstrong"];
//$a1 = ["arp", "live", "strong"];
$a1 = array(1.9, 'ou', 've', 'ect', 'omm', 'gla', 'oint', 'pini', 'wh', 'oes', 'by', 'ion', 'or', 'he', 'ple', 'ing');
$a2 = array('you', '', 'In', '1.9.2.', 'for', 'does', '', '', '', 'me', '', '', '', 'I', '', 'Ruby', 'the', '', '');
// expected 1.9, by, he, oes, or, ou
inArray($a1, $a2);
