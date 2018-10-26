/**
 * Write a function called repeatStr which repeats the
 * given string string exactly n times
 */

/**
 * 
 * @param {integer} n 
 * @param {string} s 
 */
function repeatStr (n, s) {
    var new_string = '';
    while (n > 0) {
        new_string += s;
        n--;
    }
    return new_string;
}
