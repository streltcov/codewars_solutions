<?php

function sqInRect($lng, $wdth) {

    // checking initial figure
    if ($lng == $wdth) return null;
    //
    $lng - $wdth > 0 ? $sides = [$lng, $wdth] : $sides = [$wdth, $lng];
    $result = array();

    /**
     * check sides - if equal - square
     *
     * @param array $sides
     * @return boolean
     */
    $isSquare = function(array $sides) {
        if ($sides[0] == $sides[1]) {
            return true;
        } else {
            return false;
        }
    }; // end function

    /**
     * @return array
     */
    $square = function($sides, $result) use(&$square, $isSquare) {
        echo "Current sides".PHP_EOL;
        print_r($sides);
        $sides[0] - $sides[1] > 0? $result[] = $sides[1] : $result[] = $sides[0];
        if ($isSquare($sides)) {
            $result[] = $sides[0];
            return $result;
        } else {
            $sides[0] - $sides[1] > 0 ? $sides = [$sides[0] - $sides[1], $sides[1]] : $sides = [$sides[1] - $sides[0], $sides[0]];
            return $square($sides, $result);
        }
    }; // end function

    $figure = $square($sides, $result);
    $last = array_pop($figure);
    return $figure;

} // end function

var_dump(sqInRect(3, 5));
