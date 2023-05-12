/**
 * Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative
 * or non-integer. If the array does not contain any numbers then you should return 0;
 *
 * Examples
 *      Input: [1, 5.2, 4, 0, -1]
 *      Output: 9.2
 *
 *      Input: []
 *      Output: 0
 *
 *      Input: [-2.398]
 *      Output: -2.398
 *
 * Assumptions
 *      - You can assume that you are only given numbers;
 *      - You cannot assume the size of the array;
 *      - You can assume that you do get an array and if the array is empty, return 0;
 *
 * URL: https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/javascript
 */

// Sum Numbers
function sum (numbers) {
    "use strict";
  const sum = numbers.reduce((partial, element) => partial + element, 0);
  return sum;
};
