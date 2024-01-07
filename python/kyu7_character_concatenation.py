"""
Given a string, you progressively need to concatenate the first letter from the left and the first letter to the right
and "1", then the second letter from the left and the second letter to the right and "2", and so on;
If the string's length is odd drop the central element;

For example:
    char_concat("abcdef")    == 'af1be2cd3'
    char_concat("abc!def")   == 'af1be2cd3' # same result

https://www.codewars.com/kata/55147ff29cd40b43c600058b;

"""


def char_concat(word):
    result, counter = '', 1
    while len(word) > 1:
        result = result + word[0] + word[-1] + str(counter)
        word, counter = word[1:-1], counter + 1
    
    return result
