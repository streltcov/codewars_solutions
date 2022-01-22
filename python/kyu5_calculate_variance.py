""" Write a function which will accept a sequence of numbers and calculate the variance for the sequence;
The variance for a set of numbers is found by subtracting the mean from every value, squaring the results, adding
them all up and dividing by the number of elements;

Examples:
    variance([8, 9, 10, 11, 12]), 2)
    variance([1.5, 2.5, 4, 2, 1, 1]), 1.0833333333333333)

"""


def variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum(list(map(lambda x: (x - mean) ** 2, numbers))) / len(numbers)
