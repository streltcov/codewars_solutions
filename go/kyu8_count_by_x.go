// Create a function with two arguments that will return an array of the first n multiples of x;
//
// Assume both the given number and the number of times to count will be positive numbers greater than 0;
//
// Return the results as an array or list (depending on language);
//
// https://www.codewars.com/kata/5513795bd3fafb56c200049e
//


package kata


func CountBy(x, n int) []int {
  result := []int{x}
  accumulator := x
  
  for i := 1; i < n; i++ {
    accumulator = accumulator + x
    result = append(result, accumulator)
  }
  
  return result
}
