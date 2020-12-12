"""
Acknowledgments:
I thank yvonne-liu for the idea and for the example tests :)

Description: Encrypt this!
You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:
    1. Your message is a string containing space separated words
    2. You need to encrypt each word in the message using the following rules:
        * The first letter needs to be converted to its ASCII code
        * The second letter needs to be switched with the last letter
    3. Keepin' it simple: There are no special characters in input

Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
"""


def encrypt_this(text):
    """
    :param text: string parameter; a sentence containing several words, each of which must be encrypted according
    to the specified rules
    :type text: str
    :rtype: str
    :return: encrypted sentence
    """
    encrypted = ''
    text = text.split()
    for word in text:
        first_char, word = str(ord(word[:1])), word[1:]
        second_char, word = word[:1], word[1:]
        last_char, word = word[-1:], word[:-1]
        encrypted += first_char + last_char + word + second_char + ' '
    return encrypted[:-1]
