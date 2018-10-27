<?php

/**
 * Write function heron which calculates the area of a triangle with sides a, b, and c
 * Heron's formula: sqrt (s * (s - a) * (s - b) * (s - c)), where s = (a + b + c) / 2
 */

/**
 * solution
 */

function heron($a, $b, $c)
{
  $s = ($a + $b + $c) / 2;
  return sqrt($s * ($s - $a) * ($s - $b) * ($s - $c));
}
