"""
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result
should be {'a': 2, 'b': 1}

What if the string is empty? Then the result should be empty object literal, {}
"""


def count(string):
    """
    :param string: the string in which to count the occurrences of characters;
    :return: a dictionary containing a count of occurrences of characters;
    """
    counts = {}
    for char in string:
        counts[char] = string.count(char)
    return counts
