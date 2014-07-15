import sys

class RG(object):
    def __init__(self, r, s, m, xs):
        self.r, self.s, self.m, self.xs = r,s, m, xs
        self.p = xs[-1]
        self.c = 0

    def get(self):
        p = self.xs[-self.s] - self.xs[-self.r] - self.c
        self.c = 1 if p<0 else 0
        ret = p % self.m
        assert(0 <= ret < self.m)
        self.xs = self.xs[1:] + [ret]
        return ret

rg = RG(43, 22, 2**32, [999999999*(i**3)%(2**32) for i in range(0, 42+1)])
assert(rg.get()==1050500563)
assert(rg.get()==4071029865)
assert(rg.get()==4242540160)

def shift(state, d):
    n, p = 0, -1
    new_state = []
    p = 0
    if d=='r':
        state = list(reversed(state))
    for s in (x for x in state if x>0):
        if p>=0 and p == s: # merge!
            new_state.pop()
            new_state.append(s*2)
            p = -1
        else:
            new_state.append(s)
            p = s
    if d=='r':
        new_state = list(reversed(new_state))
    return new_state

for _ in'*'*input():
    raw_input()
    N = input()
    INITIAL = map(int, raw_input().strip().split())
    XS = [int(x) for x in raw_input().strip().split()]
    input()
    INPUT = raw_input().strip()
    state = INITIAL
    rg = RG(43, 22, 2**32, XS)
    for d in INPUT:
        new_state = shift(state, d)
        empty = [0] * (N - len(new_state))
        if not empty:
            break
        if (d=='l' and new_state+empty==state) or \
            (d=='r' and empty+new_state==state):
            continue
        state = new_state
        p = rg.get() % len(empty)
        v = 4 if (rg.get() % 10) == 0 else 2
        empty[p] = v
        if d=='l':
            state = state + empty
        else:
            state = empty + state
    print ' '.join(str(x) for x in state)
