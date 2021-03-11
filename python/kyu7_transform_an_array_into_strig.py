def transform(s):
    """ A simple kata, my first;
    Simply tranform an array into a string;

    Examples:
        transform([4, -56, true, "box"]) => "4-56truebox"

    Args:
        s (list): a sequence to be transformed into string

    Returns:
        str: transformed array
    """
    return ''.join([str(x) for x in s])
