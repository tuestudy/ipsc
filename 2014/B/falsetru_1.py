import itertools
from collections import deque


r, s, m = 43, 22, 2 ** 32

def make_prg(seeds, r, s, m):
    c = deque([0] * r, maxlen=r)
    seeds = deque(seeds, maxlen=r)
    while 1:
        x = seeds[-s] - seeds[-r] - c[-1]
        y = x % m
        yield y
        seeds.append(y)
        c.append(int(x < 0))


def step(state, direction):
    new = []
    prev = 0
    for x in (state if direction == 'l' else reversed(state)):
        if not x: continue
        if x == prev:
            new.append(x*2)
            prev = 0
        else:
            if prev:
                new.append(prev)
            prev = x
    if prev:
        new.append(prev)
    nempty = len(state) - len(new)
    new += [0] * nempty
    if direction == 'r':
        new.reverse()
    return new

def move(state, rng, direction):
    old = state
    state = step(state, direction)
    if old != state:
        n0 = sum(x == 0 for x in state)
        pos = next(rng) % n0
        if direction == 'l':
            pos += len(state) - n0
        state[pos] = 4 if next(rng) % 10 == 0 else 2
    return state

def solve(state, rng, directions):
    for d in directions:
        state = move(state, rng, d)
    return state

if __name__ == '__main__':
    for i in range(input()):
        blank_line = raw_input(); n = raw_input()
        state = map(int, raw_input().split())
        seeds = map(int, raw_input().split())
        a = raw_input()
        directions = raw_input()
        state = solve(state, make_prg(seeds,r,s,m), directions)
        print ' '.join(map(str, state))
