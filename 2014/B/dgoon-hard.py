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

def shift(state, d):
    score_added = 0
    n, p = 0, -1
    new_state = []
    p = 0
    if d=='r':
        state = list(reversed(state))
    for s in (x for x in state if x>0):
        if p>=0 and p == s: # merge!
            new_state.pop()
            new_state.append(s*2)
            score_added += s*2
            p = -1
        else:
            new_state.append(s)
            p = s
    if d=='r':
        new_state = list(reversed(new_state))
    return new_state, score_added

for _ in'*'*input():
    raw_input()
    N = input()
    INITIAL = map(int, raw_input().strip().split())
    XS = [int(x) for x in raw_input().strip().split()]

    state = tuple(INITIAL)
    rg = RG(43, 22, 2**32, XS)

    max_score = 0
    iteration = 0
    queue = {state: 0}

    while queue:
        iteration += 1
        next_queue = {}
        r = rg.get()
        v = 4 if (rg.get() % 10) == 0 else 2

        for state, score in queue.iteritems():
            for d in 'lr':
                new_state, score_added = shift(state, d)
                new_score = score + score_added
                max_score = max(new_score, max_score)
                new_state = tuple(new_state)

                empty = [0] * (N - len(new_state))
                t_empty = tuple(empty)
                finished = (d=='l' and new_state+t_empty==state) or \
                           (d=='r' and t_empty+new_state==state)

                #print d, new_state, '->', new_state, score_added, '(%d)' % new_score
                if finished:
                    #print('Finished: %d', score)
                    continue

                p = r % len(empty)
                empty[p] = v
                empty = tuple(empty)
                if d=='l': new_state = new_state + empty
                else:      new_state = empty + new_state
                new_state = tuple(new_state)
                stored_score = next_queue.get(new_state, None)
                if stored_score is None or \
                   stored_score and stored_score<new_score:
                    next_queue[new_state] = new_score

        queue = next_queue
    print max_score
