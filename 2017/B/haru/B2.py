# -*- encoding: utf-8 -*-

from sys import stdin

def solve_white(rows, cols):
    if rows == 1:
        if cols == 2:
            return [(0, 0)]
        else:
            return []
    elif rows == 2:
        result = []
        for c in range(cols):
            if c % 2 == 0:
                result.append((0, c))
            else:
                result.append((1, c))
        return result
    else:
        return []

# move clockwise
def solve_odd_square_black(n):
    result = [(1, 0)]
    count = (n * n) // 2
    move = 'right'
    top, left, bottom, right = 0, 0, n - 1, n - 1

    while len(result) != count:
        assert len(result) == len(set(result)), 'contain duplicated item: {}'.format(result)

        cur_r, cur_c = result[-1]
        # print("current direction", move)
        if move == 'right':
            next_r = cur_r + 1 if cur_r == top else cur_r - 1
            next_c = cur_c + 1
        elif move == 'left':
            next_r = cur_r - 1 if cur_r == bottom else cur_r + 1
            next_c = cur_c - 1
        elif move == 'top':
            next_r = cur_r - 1
            next_c = cur_c + 1 if cur_c == left else cur_c - 1
        elif move == 'bottom':
            next_r = cur_r + 1
            next_c = cur_c - 1 if cur_c == right else cur_c + 1

        if top <= next_r <= bottom and left <= next_c <= right:
            result.append((next_r, next_c))
            continue

        # should change direction
        if cur_c == right:  # move bottom
            top = cur_r + 1
            move = 'bottom'
        elif cur_c == left: # move top
            bottom = cur_r - 1
            move = 'top'
        elif cur_r == top:  # move right
            left = cur_c + 1
            move = 'right'
        elif cur_r == bottom:   # move left
            right = cur_c - 1
            move = 'left'
    return result

# move counterclock wise
def solve_odd_black(rows, cols):
    result = [(0, 1)]
    count = (rows * cols) // 2
    move = 'bottom'
    top, left, bottom, right = 0, 0, rows - 1, cols - 1
    while len(result) != count:
        assert len(result) == len(set(result)), 'contain duplicated item: {}'.format(result)

        cur_r, cur_c = result[-1]

        if move == 'right':
            next_r = cur_r - 1 if cur_r == bottom else cur_r + 1
            next_c = cur_c + 1
        elif move == 'left':
            next_r = cur_r + 1 if cur_r == top else cur_r - 1
            next_c = cur_c - 1
        elif move == 'top':
            next_r = cur_r - 1
            next_c = cur_c - 1 if cur_c == right else cur_c + 1
        elif move == 'bottom':
            next_r = cur_r + 1
            next_c = cur_c + 1 if cur_c == left else cur_c - 1

        if top <= next_r <= bottom and left <= next_c <= right:
            result.append((next_r, next_c))
            continue

        old_move = move
        # should change direction
        if cur_c == right:      # right -> top
            bottom = cur_r - 1
            move = 'top'
        elif cur_c == left:     # left -> bottom
            top = cur_r + 1
            move = 'bottom'
        elif cur_r == top:      # top -> left
            right = cur_c - 1
            move = 'left'
        elif cur_r == bottom:   # bottom -> right
            left = cur_c + 1
            move = 'right'
    return result

def solve_black(rows, cols):
    if rows == 1:
        if cols <= 3:
            return [(0, 1)]
        else:
            return []
    elif rows == 2:
        result = []
        for c in range(cols):
            if c % 2 == 0:
                result.append((1, c))
            else:
                result.append((0, c))
        return result
    elif rows == 3 and cols == 3:
        return [(1, 0), (0, 1), (1, 2), (2, 1)]
    elif rows % 2 == 1:
        if rows == cols:
            return solve_odd_square_black(rows)
        elif cols - rows == 2:
            return solve_odd_black(rows, cols)
    return []

def solve(rows, cols, color):
    transposed = rows > cols

    if transposed:
        rows, cols = cols, rows

    if color == 'W':
        result = solve_white(rows, cols)
    else:
        result = solve_black(rows, cols)

    if transposed:
        return [(c, r) for (r, c) in result]
    else:
        return [(r, c) for (r, c) in result]


if __name__ == '__main__':
    # ignore the number of test case
    stdin.readline().strip()

    inputs = set()
    for line in stdin:
        line = line.strip()
        if len(line) > 0:
            r, c, f = line.split()
            result = solve(int(r), int(c), f)
            if len(result) == 0:
                print('impossible')
            else:
                for r, c in result:
                    print('{} {}'.format(r + 1, c + 1))
            print('') # print a blank line
