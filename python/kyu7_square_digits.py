"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them;
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1;
Note: The function accepts an integer and returns an integer
"""


def square_digits(num):
    """
    :param num: integer value;
    :return: integer value, 'concatenated' squares of all digits in num
    """
    square_digits, items = '', list(str(num))
    for item in items:
        square_digits += str(int(item) * int(item))
    return int(square_digits)
