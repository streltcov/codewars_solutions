"""
Complete the solution so that the function will break up camel casing, using a space between words;

EXAMPLE:
solution("camelCasing")  ==  "camel Casing"
"""


def solution(s):
    """
    :param s: camel case string to be divided in separate words
    :return: divided string
    """
    split_string = ''
    for char in s:
        split_string += ' ' + char if char.istitle() else char
    return split_string
