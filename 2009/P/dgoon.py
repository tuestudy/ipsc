#! /usr/bin/env python3
#-*- encoding: utf-8 -*-

DIFF = {
    (0, 1): 'R',
    (0, -1): 'L',
    (1, 0): 'D',
    (-1, 0): 'U',
}

def get_diff(direction):
    for k, v in DIFF.items():
        if v==direction:
            return k

def possible_direction(maze, pos):
    R, C = len(maze), len(maze[0])
    cur_x, cur_y = pos
    ret = []
    for (dx, dy), direction in DIFF.items():
        x = cur_x + dx
        y = cur_y + dy
        if x<0 or x>=R or y<0 or y>=C:
            continue
        if maze[x][y]!=1:
            ret.append(direction)
    return ret

def move(maze, cur, direction):
    cur_x, cur_y = cur
    dx, dy = get_diff(direction)
    assert(maze[cur_x][cur_y]==8)
    maze[cur_x][cur_y] = 1
    new_x, new_y = cur_x+dx, cur_y+dy
    maze[new_x][new_y] = 8
    return new_x, new_y

def blocked(maze, pos):
    cur_x, cur_y = pos
    wall_cnt = 0
    for (dx, dy), _ in DIFF.items():
        x = cur_x+dx
        y = cur_y+dy
        if not (0<=x<len(maze) and 0<=y<len(maze[0])):
            continue
        wall_cnt += 1 if maze[x][y]==1 else 0
    return wall_cnt==3

def fill_blocked(maze):
    R, C = len(maze), len(maze[0])
    for r in range(R):
        for c in range(C):
            if maze[r][c]!=0:
                continue
            if blocked(maze, (r, c)):
                maze[r][c]=1

def exit_pos(maze):
    R = len(maze)
    C = len(maze[0])
    for r in range(R):
        for c in range(C):
            if r not in (0, R-1) and c not in (0, C-1):
                continue
            if maze[r][c]==0:
                return r, c

def print_maze(maze):
    for row in maze:
        print(' '.join(str(x) for x in row))
    print()

def escape(maze, start):
    cur = start
    destination = exit_pos(maze)
    moves = []
    while cur != destination:
        d = None
        while True:
            d = possible_direction(maze, cur)
            if len(d)>1:
                fill_blocked(maze)
            else:
                break
        assert(len(d)>0)
        cur = move(maze, cur, d[0])
        moves.append(d[0])
    moves.append(moves[-1])
    return ' '.join(str(x) for x in moves)

R, C = [int(x) for x in input().strip().split()]
maze = []
for r in range(R):
    maze.append([int(x) for x in input().strip().split()])

start_x, start_y = [int(x)-1 for x in input().strip().split()]
maze[start_x][start_y] = 8 

print(escape(maze, (start_x, start_y)))
