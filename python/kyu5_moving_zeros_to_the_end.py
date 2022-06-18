""" Moving zeros to the end;

https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other
elements

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

"""


def move_zeros(array):
    return [x for x in array if x != 0] + [x for x in array if x == 0]
