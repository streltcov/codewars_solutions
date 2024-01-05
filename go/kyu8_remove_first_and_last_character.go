// It's pretty straightforward. Your goal is to create a function that removes the first and last characters of
// a string. You're given one parameter, the original string. You don't have to worry with strings with less than
// two characters;
//
// https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0 
//

package kata


func RemoveChar(word string) string {
    trimedWord := ""
    wordLen := len(word) - 1
    
    for i, char := range word {
		  if i != 0 {
        if i != wordLen {
			    trimedWord = trimedWord + string(char)
		    }
		  }
	  }
    
    return trimedWord
}
