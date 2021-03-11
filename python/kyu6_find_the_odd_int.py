from collections import Counter


def find_it(seq):
    """ Given an array of integers, find the one that appears an odd number of times;
    There will always be only one integer that appears an odd number of times;

    Examples:
        find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) => 5

    Args:
        seq (list): a sequence where only one of the elements occurs an odd number of times

    Returns:
        int: odd integer, the number of times an element occurs in a sequence
    """
    counter = list(zip(Counter(seq).keys(), Counter(seq).values()))
    return [x[0] for x in counter if x[1] % 2 != 0][0]
