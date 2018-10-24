<?php

function reverser(string $sentence) {
  $sentence = explode(" ", $sentence);
  foreach ($sentence as $word) {
      $word = implode(array_reverse(str_split($word)));
      $result[] = $word;
    }
  return implode(" ", $result);
}

$a = reverser('sentence is sentence');
print_r($a);
