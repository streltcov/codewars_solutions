"""
Create a function that takes an integer as an argument and returns 'Even' for even
numbers or 'Odd' for odd numbers
"""


def even_or_odd(number):
    """
    :param number: an integer number to be tested
    :return: string - 'Even' or 'Odd'
    """
    if number % 2 ==0:
        return 'Even'
    return 'Odd'
