"""

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers;

Return your answer as a number;

https://www.codewars.com/kata/57eaeb9578748ff92a000009

"""


def sum_mix(arr):
    return sum([float(item) for item in arr])
