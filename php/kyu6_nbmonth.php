<?php

function nbMonths($startPriceOld, $startPriceNew, $savingPerMonth, $percentLossByMonth) {
    $month = function($price1, $price2, $saving, $loss, $acc) use(&$month) {
        if ($acc != 0) {
            if($acc % 2 != 0) {
                $loss = $loss + 0.5;
            }
        }
        if ($price1 + $saving * $acc >= $price2) {
            return [$acc, (int)round((($price1 + $saving * $acc) - $price2), 0)];
        } else {
            return $month(($price1 - ($price1 * $loss) / 100), ($price2 - ($price2 * $loss) / 100), $saving, $loss, $acc + 1);
        }
    };

    return $month($startPriceOld, $startPriceNew, $savingPerMonth, $percentLossByMonth, 0);
}

//$a = nbMonths(2000, 8000, 1000, 1.5); // 6, 766
//$b = nbMonths(8000, 12000, 500, 1); //8, 597
$c = nbMonths(2600, 3200, 1000, 1.3);
print_r($c);
