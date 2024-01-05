// Very simple, given an integer or a floating-point number, find its opposite;
//
// Examples:
//		1: -1
//		14: -14
//		-34: 34
//
// https://www.codewars.com/kata/56dec885c54a926dcd001095
//


package kata

func Opposite(value int) int {
    result := value * (-1)
    return result
}
