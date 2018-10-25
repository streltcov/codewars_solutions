<?php

$alphabet = [
  1 => 'a', 2 => 'b', 3 => 'c', 4 => 'd', 5 => 'e',
  6 => 'f', 7 => 'g', 8 => 'h', 9 => 'i', 10 => 'j',
  11 => 'k', 12 => 'l', 13 => 'm', 14 => 'n', 15 => 'o',
  16 => 'p', 17 => 'q', 18 => 'r', 19 => 's', 20 => 't',
  21 => 'u', 22 => 'v', 23 => 'w', 24 => 'x', 25 => 'y',
  26 => 'z'
];

function high($s)
{
  global $alphabet;
  $score = function($word) use($alphabet) {
    $word_score = 0;
    $letters = str_split($word);
    foreach ($letters as $letter) {
      if (in_array($letter, $alphabet)) {
        $word_score = $word_score + array_search($letter, $alphabet);
      }
    }
    return $word_score;
  };

  $words = explode(' ', $s);
  foreach ($words as $key => $word) {
    $scores[$key] = $score($word);
  }
  $max_value = array_search(max($scores), $scores);
  return $words[$max_value];
}

//echo high('abca abc') . PHP_EOL;
echo high('what time are we climbing up the volcano') . PHP_EOL;
