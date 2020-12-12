"""
The idea for this Kata came from 9gag today.here

You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet) wiki

Like this:

INPUT:
    If, you can read?

OUTPUT:
    India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?

NOTES:
    The set of used punctuation is .!?.
    Punctuation should be kept in your return string, but spaces should not.
    Xray should not have a dash within.
    Every word and punctuation mark should be seperated by a space ' '.
    There should be no trailing whitespace
"""


def to_nato(words):
    """
    :param words: string parameter; words to be encoded with NATO phonetic alphabet codes;
    :type words: str
    :rtype: str
    :return: string encoded with NATO phonetic alphabet
    """
    alphabet = {'a': 'Alfa', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo', 'f': 'Foxtrot',
                'g': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliett', 'k': 'Kilo', 'l': 'Lima',
                'm': 'Mike', 'n': 'November', 'o': 'Oscar', 'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo',
                's': 'Sierra', 't': 'Tango', 'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey',
                'y': 'Yankee', 'x': 'Xray', 'z': 'Zulu'}
    nato = ''
    for char in words:
        if char != ' ':
            nato += alphabet[char.lower()] + ' ' if char.lower() in alphabet.keys() else char + ' '
    return nato[:-1]
