// Kata Task
//
// I have a cat and a dog;
//
// I got them at the same time as kitten/puppy. That was humanYears years ago;
// Return their respective ages now as [humanYears,catYears,dogYears];
//
// Note:
//		humanYears >= 1
//		humanYears are whole numbers only
//
// Cat Years
//    15 cat years for first year
//    +9 cat years for second year
//    +4 cat years for each year after that
//
// Dog Years
//    15 dog years for first year
//    +9 dog years for second year
//    +5 dog years for each year after that
//
// https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b
//


package kata


func CalculateYears(years int) (result [3]int) {
  catYears := 0
  dogYears := 0
  
  for i := 1; i <= years; i++ {
      switch i {
          case 1:
            catYears += 15
          case 2:
            catYears += 9
          default:
            catYears += 4
      }
  }
  
  for i := 1; i <= years; i++ {
      switch i {
          case 1:
            dogYears += 15
          case 2:
            dogYears += 9
          default:
            dogYears += 5
      }
  }
  
  result = [3]int{years, catYears, dogYears}
  return result
}
