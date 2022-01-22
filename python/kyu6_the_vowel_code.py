"""
Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according
to the following pattern:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5

For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata


Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown
above
For example, decode("h3 th2r2") would return "hi there"
For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels

"""

vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5, 'A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5,}


def encode(st):
    encode_char = lambda char: char if char not in vowels.keys() else str(vowels.get(char, ''))
    return ''.join([encode_char(a) for a in st])


def decode(st):
    inversed_vowels = {str(v): str(k) for k, v in vowels.items()}
    decode_char = lambda char: char if char not in inversed_vowels.keys() else str(
        inversed_vowels.get(char, '')).lower()
    return ''.join([decode_char(a) for a in st])
