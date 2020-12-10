"""
Return the number (count) of vowels in the given string;
We will consider a, e, i, o, u as vowels for this Kata (but not y);
The input string will only consist of lower case letters and/or spaces
"""


def get_count(input_str):
    """
    :param input_str: string containing some vowels
    :type: str
    :return: number of vowels in given string
    :rtype: int
    """
    num_vowels = 0
    vowels = ('a', 'e', 'i', 'o', 'u')
    for character in input_str:
        if character in vowels:
            num_vowels += 1
    return num_vowels
