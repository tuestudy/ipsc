# -*- encoding: utf-8 -*-

from sys import stdin

def is_whole_world_flooded(world, rows, cols):
    return sum(sum(r) for r in world) == rows * cols

def is_valid_pos(rows, cols, pos):
    return 0 <= pos[0] < rows and 0 <= pos[1] < cols

def can_flood(world, rows, cols, pos):
    direction = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
    count = 0
    for dr, dc in direction:
        r = pos[0] + dr
        c = pos[1] + dc
        if is_valid_pos(rows, cols, (r, c)):
            count += world[r][c]
    return count > 1

def flood(world, rows, cols):
    while 1:
        changed = False
        for r in range(rows):
            for c in range(cols):
                if world[r][c] != 1 and can_flood(world, rows, cols, (r, c)):
                    world[r][c] = 1
                    changed = True
        if is_whole_world_flooded(world, rows, cols):
            return world
        if not changed:
            return world


def click_world(rows, cols, clicks):
    world = [[0] * cols for i in range(rows)]
    for (r, c) in clicks:
        world[r][c] = 1
    return world

def solve(rows, cols, check_validation = False):
    k = min(rows, cols)

    # click diagonals
    clicks = []
    for i in range(k):
        clicks.append((i, i))

    if rows < cols:
        for i in range(k + 1, cols, 2):
            clicks.append((rows - 1, i))
    elif cols < rows:
        for i in range(k + 1, rows, 2):
            clicks.append((i, cols - 1))

    if abs(rows - cols) % 2 == 1:
        clicks.append((rows - 1, cols - 1))

    if check_validation:
        world = flood(click_world(rows, cols, clicks), rows, cols)
        if not is_whole_world_flooded(world, rows, cols):
            exit(1)

    return clicks

if __name__ == "__main__":
    # ignore the number of test case
    stdin.readline().strip()

    for line in stdin:
        line = line.strip()
        if len(line) > 0:
            r, c = [int(x) for x in line.split()]
            result = solve(r, c)
            print(len(result))
            for (x, y) in result:
                print(x, y)
