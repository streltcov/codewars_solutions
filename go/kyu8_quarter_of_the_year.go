// Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number;
//
// For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter;
// and month 11 (November), is part of the fourth quarter;
//
// Constraint:
//		1 <= month <= 12
//
// https://www.codewars.com/kata/5ce9c1000bab0b001134f5af
//


package kata


func QuarterOf(month int) int {
    firstQuarter := map[int]bool{1: true, 2: true, 3: true}
    secondQuarter := map[int]bool{4: true, 5: true, 6: true}
    thirdQuarter := map[int]bool{7: true, 8: true, 9: true}
    fourthQuarter := map[int]bool{10: true, 11: true, 12: true}
    quarter := 0
  
    if firstQuarter[month] {
        quarter = 1
    }
  
    if secondQuarter[month] {
        quarter = 2
    }
    
    if thirdQuarter[month] {
        quarter = 3
    }
    
    if fourthQuarter[month] {
        quarter = 4
    }
    
    return quarter
}
