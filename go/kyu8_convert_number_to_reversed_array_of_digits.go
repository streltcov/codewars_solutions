// Given a random non-negative number, you have to return the digits of this number within an array in reverse order;
//
// https://www.codewars.com/kata/5583090cbe83f4fd8c000051
//


package kata

import (
  "strconv"
  "strings"
)


func Digitize(n int) []int {
  n_str := strconv.Itoa(n)
  strArray := strings.Split(n_str, "")
  digits := []int{}
  
  for i := 0; i < len(strArray); i++ {
    currentDigit, _ := strconv.Atoi(strArray[i])
    digits = append(digits, currentDigit)
  }
  
  reversed_digits := []int{}
  
  for i := len(digits) - 1; i >= 0; i-- {
    reversed_digits = append(reversed_digits, digits[i])
  }
  
  return reversed_digits
}
