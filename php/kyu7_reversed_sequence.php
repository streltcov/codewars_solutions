<?php

/**
 * Take a sentence (string) and reverse each word in the sentence. Do not reverse the
 * order of the words, just the letters in each word
 * If there is punctuation, it should be interpreted as a regular character; no special rules
 * 
 * If there is spacing before/after the input string, leave them there
 * String will not be empty
 */

/**
 * solution
 */

function reverser(string $sentence) {
  $sentence = explode(" ", $sentence);
  foreach ($sentence as $word) {
      $word = implode(array_reverse(str_split($word)));
      $result[] = $word;
    }
  return implode(" ", $result);
}
