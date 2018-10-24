<?php

function solution($str) {
    return implode('', array_reverse(str_split($str)));
}
