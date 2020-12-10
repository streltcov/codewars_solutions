"""
Given the triangle of consecutive odd numbers:
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...

Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:
row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5
"""


def row_sum_odd_numbers(n):
    """
    :param n: number of row
    :type n: int
    :rtype: int
    :return: sum of items from row with a number given as argument
    """
    sum, start = 1, 0
    if n == 1:
        return sum
    for i in range(1, n):
        start += i * 2
    item = start + 1
    for i in range(0, n):
        sum += item
        item = item + 2
    return sum - 1
