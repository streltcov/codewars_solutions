/**
 * Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive
 * integers. No floats or non-positive integers will be passed;
 * 
 * For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7;
 *      [10, 343445353, 3453445, 3453545353453] should return 3453455.
 * 
 * https://www.codewars.com/kata/558fc85d8fd1938afb000014
 * 
 */


function sumTwoSmallestNumbers(numbers) {
    function compareNumeric(a, b) {
        if (a > b) return 1;
        if (a == b) return 0;
        if (a < b) return -1;
    }
    
    numbers.sort(compareNumeric);
    let first = numbers.shift();
    let second = numbers.shift();
    return first + second;
}
