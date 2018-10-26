/**
 * You get an array of numbers, return the sum of all of the positives ones
 * Example [1,-4,7,12] => 1 + 7 + 12 = 20
 * 
 * Note: if there is nothing to sum, the sum is default to 0
 */

/**
 * 
 * @param {array} arr
 */
function positiveSum(arr) {
    arr = arr.filter(function(item) {
        return item > 0;
    });
    if (arr.length > 0) {
        var sum_arr = arr.reduce(function(sum, current) {
            return sum + current;
        });
        return sum_arr;
    }
    return 0;
}
