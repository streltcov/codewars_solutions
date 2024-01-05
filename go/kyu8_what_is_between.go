// Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the
// input parameters, including them;
//
// Example:
//		a = 1
//		b = 4
//		Between(a, b) ---> [1, 2, 3, 4]
//
// https://www.codewars.com/kata/55ecd718f46fba02e5000029
//


package kata


func Between(a, b int) []int {
    result := []int{a}
    
    for i := a + 1; i < b; i++ {
        result = append(result, i)
    }
  
    result = append(result, b)
    return result
}
