#/usr/bin/env python
import unittest
import sys

class RandomGenerator:
    def __init__(self, arr):
        self.randoms = arr
        self.curr = 43
        self.c = [0 for x in xrange(43)]

    def random(self):
        r = 43
        s = 22
        m = 2 ** 32
        val = self.randoms[self.curr - s] - self.randoms[self.curr - r] - self.c[self.curr - 1]
        self.randoms.append(val % m)
        self.c.append(1 if val < 0 else 0)
        self.curr += 1
        return self.randoms[self.curr - 1]

def applymove(diagram, move, rg):
    if move not in ['l', 'r']:
        return
    lastval = -1
    newdiagram = []
    if move == 'l':
        for val in diagram:
            if val == 0:
                continue
            if val == lastval:
                newdiagram[-1] = val + lastval
                lastval = -1
            else:
                newdiagram.append(val)
                lastval = val
    else:
        for val in reversed(diagram):
            if val == 0:
                continue
            if val == lastval:
                newdiagram[0] = val + lastval
                lastval = -1
            else:
                newdiagram.insert(0, val)
                lastval = val

    num_empty = len(diagram) - len(newdiagram)
    if num_empty == 0:
        return newdiagram

    emptycells = [0 for _ in xrange(num_empty)]
    offset = 0

    if move == 'l':
        offset = len(newdiagram)
        newdiagram.extend(emptycells)
    else:
        emptycells.extend(newdiagram)
        newdiagram = emptycells

    if diagram == newdiagram:
        return newdiagram

    (new_value, pos) = getRandomNumber(rg, num_empty)
    newdiagram[offset + pos] = new_value
    return newdiagram

def getRandomNumber(rg, num_empty):
    pos = rg.random() % num_empty
    new_value = 0
    if rg.random() % 10 == 0:
        new_value = 4
    else:
        new_value = 2
    return (new_value, pos)


class Test(unittest.TestCase):
    def test_def(self):
        pass

def main(stdin, stdout):
    casecount = int(stdin.readline())
    for case in range(casecount):
        stdin.readline()
        strip_size = int(stdin.readline().strip())
        diagram = [int(x) for x in stdin.readline().strip().split()]

        arr = [int(x) for x in stdin.readline().strip().split()]
        rg = RandomGenerator(arr)

        mode = 'b1'
        if mode == 'b1':
            moves_count = stdin.readline()
            moves = stdin.readline().strip()
            # b1 solution
            for move in moves:
                diagram = applymove(diagram, move, rg)
            print ' '.join(str(x) for x in diagram)
        else:
            # b2 solution
            pass

if __name__ == '__main__':
    main(sys.stdin, sys.stdout)
