# -*- coding: utf-8 -*-

"""ISBN 10 Validation;

https://www.codewars.com/kata/51fc12de24a9d8cb0e000001/train/python


ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. The last digit can be 0-9 or X, to
indicate a value of 10;

An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero

For example:
    ISBN     : 1 1 1 2 2 2 3 3 3  9
    position : 1 2 3 4 5 6 7 8 9 10

This is a valid ISBN, because:
    (1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0

"""


def valid_ISBN10(isbn):
    def has_valid_isbn_format(isbn):
        valid_literals = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'X', )
        contains_only_valid = all(char in valid_literals for char in isbn)
        has_valid_positions = all(char in valid_literals[:10] for char in isbn[:9])
        
        return contains_only_valid and has_valid_positions
    
    if len(isbn) != 10 or not has_valid_isbn_format(isbn):
        return False
    
    sum = 0
    for i in range(9):
        sum += int(isbn[i]) * (i + 1)
    
    sum += (10 if isbn[9] == 'X' else int(isbn[9])) * 10
    
    return sum % 11 == 0
