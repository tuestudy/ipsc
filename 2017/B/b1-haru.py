# -*- encoding: utf-8 -*-

from sys import stdin
from math import hypot

class Problem:
    def __init__(self, rows, cols, color):
        self.transposed = rows > cols
        if self.transposed:
            self.rows = cols
            self.cols = rows
        else:
            self.rows = rows
            self.cols = cols
        self.color = color

        if self.color == 'W':
            self.start = (0, 0)
        elif self.rows == 1:
            self.start = (0, 1)
        else:
            self.start = (1, 0)

        board_size = rows * cols
        if board_size % 2 == 0 or color == 'B':
            self.path_count = board_size // 2
        else:
            self.path_count = board_size // 2 + 1

    def get_next_position(self, path):
        r, c = path[-1]
        signs = [(-1, +1), (+1, -1)]
        candidates = set()
        for k in range(1, self.cols):
            for sr, sc in signs:
                nr = r + sr * k
                nc = c + sc * k
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    candidates.add((nr, nc))
        candidates = set(candidates) - set(path)
        next_pos = None
        if len(candidates) == 0:
            if 0 <= r + 1 < self.rows and 0 <= c + 1 < self.cols:
                next_pos = (r + 1, c + 1)
        else:
            max_distance = 0
            for (nr, nc) in candidates:
                distance = hypot(nr - r, nc - c)
                if max_distance < distance:
                    next_pos = (nr, nc)
                    max_distance = distance
                elif max_distance == distance and next_pos[1] > nc:
                    next_pos = (nr, nc)
        return next_pos

    def move(self):
        path = [self.start]
        while True:
            if len(path) == self.path_count:
                return path

            r, c = path[-1]
            if r == self.rows - 3 and c == self.cols - 3 and self.path_count - len(path) == 4:
                if (self.color == 'W' and r % 2 == c % 2) or (self.color == 'B' and r % 2 != c % 2):
                    path.append((r + 2, c + 2))
                    path.append((r + 1, c + 1))
                    path.append((r + 2, c))
                    path.append((r, c + 2))
                    return path

            next_pos = self.get_next_position(path)
            if next_pos == None:
                return []
            path.append(next_pos)

    def path(self):
        if self.rows == 1 and self.cols > 3:
            return []

        steps = self.move()

        if len(steps) != self.path_count:
            return []

        if self.transposed:
            return [(c, r) for (r, c) in steps]
        else:
            return steps


if __name__ == '__main__':
    # ignore the number of test case
    stdin.readline().strip()

    inputs = set()
    for line in stdin:
        line = line.strip()
        if len(line) > 0:
            r, c, f = line.split()
            p = Problem(int(r), int(c), f)
            result = p.path()
            if len(result) == 0:
                print('impossible')
            else:
                for r, c in result:
                    print('{} {}'.format(r + 1, + c + 1))
            print('') # print a blank line
