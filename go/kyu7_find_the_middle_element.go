// As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the
// numerical element that lies between the other two elements;
// The input to the function will be an array of three distinct numbers (Haskell: a tuple);
//
// Example:
//		gimme([2, 3, 1]) => 0
//
// 2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0;
//
// Another example (just to make sure it is clear):
//		gimme([5, 10, 14]) => 1
//
// 10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1;
//
// https://www.codewars.com/kata/545a4c5a61aa4c6916000755
//


package kata


func MinMax(array [3]int) (int, int) {
    max := array[0]
    min := array[0]
    
    for _, item := range array {
        if max < item {
            max = item
        }
        if min > item {
            min = item
        }
    }
    
    return min, max
  }


func Gimme(array [3]int) int {
  number := 0
  min_value, max_value := MinMax(array)
  
  for i := 0; i < 3; i++ {
      if array[i] != min_value && array[i] != max_value {
          number = i
      }
  }
  
  return number
}
