/**
 * Given an array of integers, return a new array with each value doubled
 * For example:
 * [1, 2, 3] --> [2, 4, 6]
 */

/**
 * @param {array} x
 */
function maps(x){
    return x.map(function(item) {
        return item * 2;
  });
}
