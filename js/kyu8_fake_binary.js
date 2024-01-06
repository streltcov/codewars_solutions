/**
 * Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return
 *  the resulting string;
 * 
 * Note: input will never be an empty string;
 * 
 * https://www.codewars.com/kata/57eae65a4321032ce000002d
 * 
 */


function fakeBin(x){
    let replace = "";
    
    for (let i = 0; i < x.length; i++) {
        if (x.charAt(i) < 5) {
            replace += '0';
        };
        if (x.charAt(i) >= 5) {
            replace += '1';
        };
    }
    
    return replace;
}
