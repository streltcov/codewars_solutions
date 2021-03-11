import math


def wallpaper(l, w, h):
    """ John wants to decorate a room with wallpaper. He wants a fool-proof method for getting it right;
    John knows that the rectangular room has a length of l meters, a width of w meters, a height of h meters. The
    standard width of the rolls he wants to buy is 52 centimeters. The length of a roll is 10 meters. He bears in mind
    however, that it’s best to have an extra length of wallpaper handy in case of mistakes or miscalculations so he
    wants to buy a length 15% greater than the one he needs;
    Last time he did these calculations he got a headache, so could you help John?

    Your function wallpaper(l, w, h) should return as a plain English word in lower case the number of rolls he must
    buy;

    Examples:
        wallpaper(4.0, 3.5, 3.0) => "ten"
        wallpaper(0.0, 3.5, 3.0) => "zero"

    Args:
        l (float): room length (can be 0)
        w (float): room width (can be 0)
        h (float): room height (can be 0)

    Returns:
        str: string value for a number of wallpaper rolls
    """
    if not l or not w or not h:
        return 'zero'
    width, length, perimeter = 0.52, 10, l * 2 + w * 2
    numbers = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
               9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
               16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty"}
    return numbers[math.ceil((((perimeter / width) * h) / length) * 1.15)]
