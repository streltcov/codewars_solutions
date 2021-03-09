def generate_row(initial, line_size):
    row, i, number = [], 0, initial
    while i < line_size:
        row.append(number)
        number += initial
        i += 1
    return row


def multiplication_table(row, col):
    """ Create a function that accepts dimensions, of Rows x Columns, as parameters in order to create a
    multiplication table sized according to the given dimensions. **The return value of the function must
    be an array, and the numbers must be Fixnums, NOT strings;

    Examples:
        multiplication_table(3,3) == [[1,2,3],[2,4,6],[3,6,9]]

    Args:
        row (int): number of rows
        col (int): number of columns

    Returns:
        list: generated table
    """
    table, row_numbers = [], list(range(1, row + 1))
    for num in row_numbers:
        table.append(generate_row(num, col))
    return table
