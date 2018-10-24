<?php

function dont_give_me_five($start, $end) {
    $count = 0;
    for ($start; $start <= $end; $start++) {
        if(!preg_match("/5/", (string)$start)) {
            $count++;
        }
    }
    return $count;
  }

  echo dont_give_me_five(4, 17);
