"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The
quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is
irrelevant);

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers
and punctuation;
"""


def is_pangram(s):
    """
    Checks if given string is a pangram;

    :param s: string to be checked
    :type: str
    :return: boolean value - True if given string is a pangram, False if not
    :rtype: bool
    """
    return not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())
