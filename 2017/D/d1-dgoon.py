import sys
from itertools import permutations

nonborings = {}
nbs = []
for digit in range(1, 4+1):
    nonborings[digit] = []
    for p in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], digit):
        if p[0] == 0: continue
        n = int(''.join(map(str, p)))
        nonborings[digit].append(n)
        nbs.append(n)

cache = {}

def solve(n, ns):
    key = (n, len(ns))
    min_length = 100000000000000000
    good_s = []
    for c in reversed(ns):
        remain = n - c
        if remain < 0:
            cache[key] = []
            return []
        if remain == 0:
            cache[key] = [c]
            return [c]
        new_ns = filter(lambda x: x <= remain, ns)
        sub_s = solve(remain, new_ns)
        s = [c] + sub_s
        if len(s) < min_length:
            good_s = s
            min_length = len(s)
        if min_length == 2:
            break
    cache[key] = good_s
    return good_s

T = int(sys.stdin.readline())
for _ in range(T):
    sys.stdin.readline()
    n = int(sys.stdin.readline())
    ns = filter(lambda x: x <= n, nbs)
    s = solve(n, ns)
    print('%d %s' % (len(s), ' '.join(map(str, s))))
