"""
Take a sentence (string) and reverse each word in the sentence. Do not reverse the order of the words, just the letters
in each word;

If there is punctuation, it should be interpreted as a regular character; no special rules;
If there is spacing before/after the input string, leave them there;
String will not be empty

Examples:
"Hi mom" => "iH mom"
" A fun little challenge! " => " A nuf elttil !egnellahc "
"""


def reverser(sentence):
    """
    :param sentence: string parameter; sentence to be reversed;
    :type sentence: str
    :rtype: str
    :return: sentence of reversed words
    """
    sentence, reversed = sentence.split(' '), ''
    for word in sentence:
        reversed += word[::-1] + ' '
    return reversed[:-1]
