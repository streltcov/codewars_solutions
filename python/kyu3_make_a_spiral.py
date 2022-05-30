""" Make a spiral

https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python

Your task, is to create a NxN spiral with a given size

For example, spiral with size 5 should look like this:
    00000
    ....0
    000.0
    0...0
    00000

"""


def spiralize(size: int) -> list:
    """ Creates a spiral of a given size; """
    # possible direction changes; keys 0 for 'right', 1 for 'down', '2' for 'left' and 3 for 'up';
    SHIFT_DIRECTION = {0: 1, 1: 2, 2: 3, 3: 0}
    # setting up initial spiral values, initial direction and starting point coordinates;
    spiral, direction, coords, shift, init = [[0] * size for _ in range(size)], 0, (0, 0), size, True

    def right(begin: tuple, shift: int, spiral: list) -> tuple:
        nonlocal init, size
        end = (coords[0], coords[1] + shift - 1)
        for i in range(begin[1], end[1] + 1):
            spiral[begin[0]][i] = 1
        return end, shift - 2 if shift != size else shift

    def down(begin: tuple, shift: int, spiral: list) -> tuple:
        end = (begin[0] + shift - 1, begin[1])
        for i in range(begin[0], end[0] + 1):
            spiral[i][begin[1]] = 1
        return end, shift

    def left(begin: tuple, shift: int, spiral: list) -> tuple:
        nonlocal init
        end, init = (begin[0], begin[1] - shift + 1), False
        for i in range(end[1], begin[1]):
            spiral[begin[0]][i] = 1
        return end, shift

    def up(begin: tuple, shift: int, spiral: list) -> tuple:
        shift -= 2
        end = (begin[0] - shift + 1, begin[1])
        for i in range(end[0], begin[0]):
            spiral[i][begin[1]] = 1
        return end, shift

    while shift > 2:
        move = right if direction == 0 else down if direction == 1 else left if direction == 2 else up
        coords, shift = move(begin=coords, shift=shift, spiral=spiral)
        if shift <= 2 and abs(coords[1] - coords[0]) < 2:
            direction = SHIFT_DIRECTION.get(direction)
            move = right if direction == 0 else down if direction == 1 else left if direction == 2 else up
            coords, shift = move(begin=coords, shift=shift, spiral=spiral)
            break
        direction = SHIFT_DIRECTION.get(direction)

    return spiral


def prints(spiral):
    """ Prints spiral row by row; """
    for row in spiral:
        for num in row:
            print(num, end='')
        print()
