def zeros(n):
    """ Write a program that will calculate the number of trailing zeros in a factorial of a given number;
    N! = 1 * 2 * 3 * ... * N
    Be careful 1000! has 2568 digits...

    Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros;

    Examples:
        zeros(6) = 1
        # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

        zeros(12) = 2
        # 12! = 479001600 --> 2 trailing zeros

    Args:
        n (int): the number in the factorial of which we want to count the number of trailing zeros;

    Returns:
        int: number of trailing zeros
    """
    count, i = 0, 5
    while n // i:
        count, i = count + n // i, i * 5
    return count
