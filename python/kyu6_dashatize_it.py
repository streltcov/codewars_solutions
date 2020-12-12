"""
Given a variable n

If n is an integer, Return a string with dash'-'marks before and after each odd integer, but do not begin or end the
string with a dash mark. If n is negative, then the negative sign should be removed

If n is not an integer, return an empty value

EXAMPLES:
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
"""


def dashatize(n):
    """
    :param n: string, integer or None to be transformed
    :rtype: str
    :return: string with dashes in correct places
    """
    if type(n) is int:
        n = abs(n)
    if type(n) is int and n > 0:
        dashed = str(n)[:1]
        dash_check = int(dashed) % 2 == 0
        for item in str(n)[1:]:
            if not dash_check:
                dashed += '-'
            if dash_check and int(item) % 2 != 0:
                dashed += '-'
            dash_check = int(item) % 2 == 0
            dashed += str(item)
        return dashed
    return str(n)
