"""
Pascal Triangle

In mathematics, Pascal's triangle is a triangular array of the binomial coefficients expressed with formula:
(nk) = n! / k! * (n - k)!
where n denotes a row of the triangle, and k is a position of a term in the row;

Task:
Write a function that, given a depth n, returns n top rows of Pascal's Triangle flattened into a one-dimensional
list/array;

Example:
n = 1: [1]
n = 2: [1,  1, 1]
n = 4: [1,  1, 1,  1, 2, 1,  1, 3, 3, 1]
"""


def pascals_triangle(number):
    """
    :param number:
    :return:
    """
    flattened_rows = []

    previous_row = []
    for x in range(number):
        next_row = [1] + [sum(previous_row[i:i + 2]) for i in range(x)]
        flattened_rows.extend(next_row)
        previous_row = next_row

    return flattened_rows
