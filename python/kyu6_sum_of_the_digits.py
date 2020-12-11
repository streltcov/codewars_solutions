"""
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until
a single-digit number is produced. The input will be a non-negative integer;

EXAMPLES:
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""


def digital_root(n):
    """
    :return: digital root for given argument
    """
    def __sum_digits(digits):
        if len(str(digits)) == 1:
            return int(digits)
        sum = 0
        for digit in str(digits):
            sum += int(digit)
        return __sum_digits(sum)

    return __sum_digits(n)
