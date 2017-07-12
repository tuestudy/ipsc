#!/usr/bin/env python
import math

def step(C) :
    if C == 0: return
    _  = input()

    r, c = map(int, input().split())
    n = math.ceil((r+c)/2)
    m = r if r <= c else c
    d = abs(c - r)

    print(n)
    for i in range(m):
        print(i, i)

    for i in range(1, d, 2):
        if r < c: print(m - 1, m + i)
        else: print(m + i, m - 1)

    if d % 2:
        if r < c: print(m - 1, m + d - 1)
        else: print(m + d - 1, m - 1)

    step(C-1)

def main():
    step (int(input()))

if __name__ == "__main__" :
    main ()
