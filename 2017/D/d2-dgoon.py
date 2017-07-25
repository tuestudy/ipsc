import sys
from itertools import permutations

nbs = []
nbs_dict = {}
with open('nonborings.txt', 'r') as fin:
    for line in fin.readlines():
        n = int(line)
        nbs_dict[n] = True
        nbs.append(n)

def solve(n):
    if n in nbs_dict:
        return [n]
    for candidate in (x for x in reversed(nbs) if x < n):
        remain = n - candidate
        if remain in nbs_dict:
            return [candidate, remain]
    assert(false)

T = int(sys.stdin.readline())
for _ in range(T):
    sys.stdin.readline()
    n = int(sys.stdin.readline())
    ns = filter(lambda x: x <= n, nbs)
    s = solve(n)
    print('%d %s' % (len(s), ' '.join(map(str, s))))
