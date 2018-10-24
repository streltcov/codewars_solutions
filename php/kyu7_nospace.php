<?php

function no_space(string $s): string {
    return implode('', array_diff(str_split($s), [' ']));
  }

  echo no_space('8 j 8   mBliB8g  imjB8B8  jl  B');
