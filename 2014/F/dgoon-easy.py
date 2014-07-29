"""
wget http://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt
"""

import os
import simplejson
from collections import defaultdict
segments = defaultdict(list)
digits = open('pi-billion.txt').read(250000000+2)[2:]

FOUND = 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512

class Sudoku(object):
    def __init__(self):
        self.rows = []
        self.cols = [0]*9
        self.count = 0

    def appendable(self, line):
        if self.count>=9:
            return False
        for i, n in enumerate(line):
            c = self.cols[i]
            if c & (1<<n):
                return False
        return True

    def append(self, line):
        if not self.appendable(line):
            return False
        self.rows.append(line)
        for i, n in enumerate(line):
            self.cols[i] |= 1 << n
        self.count += 1
        if not self.valid():
            self.pop()
            return False
        else:
            return True

    def pop(self):
        if not self.rows:
            return
        line = self.rows[-1]
        for i, n in enumerate(line):
            self.cols[i] &= ~(1 << n)
        self.count -= 1
        self.rows = self.rows[:-1]
        return self.valid()

    def valid(self):
        if self.count==3:
            a = reduce(lambda a, b: a|b, self.cols[0:3])
            b = reduce(lambda a, b: a|b, self.cols[3:6])
            c = reduce(lambda a, b: a|b, self.cols[6:9])
            return a==b==c==FOUND
        elif self.count==6:
            a = reduce(lambda a, b: a&b, self.cols[0:3])
            b = reduce(lambda a, b: a&b, self.cols[3:6])
            c = reduce(lambda a, b: a&b, self.cols[6:9])
            return a==b==c==0

        return True

def test_sudoku():
    sudoku = Sudoku()
    assert(sudoku.append([6,3,1,2,7,9,4,8,5]))
    assert(sudoku.append([2,4,5,1,3,8,6,7,9]))
    assert(sudoku.append([2,4,5,1,3,8,6,7,9]) == False)
    assert(sudoku.append([7,8,9,4,5,6,1,2,3]))
    assert(sudoku.count == 3)
    assert(sudoku.append([1,2,3,5,4,7,8,9,6]))
    assert(sudoku.append([4,5,6,8,9,1,2,3,7]))
    assert(sudoku.append([3,1,4,7,2,5,9,6,8]) == False)
    assert(sudoku.append([8,9,7,3,6,2,5,1,4]))
    assert(sudoku.count == 6)
    assert(sudoku.append([3,1,4,7,2,5,9,6,8]))
    assert(sudoku.append([5,6,2,9,8,3,7,4,1]))
    assert(sudoku.append([9,7,8,6,1,4,3,5,2]))
    assert(sudoku.count == 9)
    assert(sudoku.valid())

test_sudoku()

if os.path.exists('segments.json'):
    print('Reading from json...')
    segments = simplejson.loads(open('segments.json', 'rb').read())
else:
    print('Generating segment info')
    current = [0] * 8
    flag = 0
    for offset in range(len(digits)-9):
        current = digits[offset:offset+9]
        if '0' not in current and len(set(current))==9:
            segments[current].append(offset+1)

    print('Total %d unique permutations are found!' % len(segments))

    print('Writing to json...')
    with open('segments.json', 'wb') as fout:
        fout.write(simplejson.dumps(segments))

def find_sudoku(s, elements):
    if s.count == 9:
        return s
    for e in elements:
        if s.append(e):
            #print('appended')
            #print('\n'.join(''.join(str(y) for y in x) for x in s.rows))
            #print
            r = find_sudoku(s, elements)
            if r:
                return r
            else:
                s.pop()
    return False

s = Sudoku()
elements = sorted([map(int, x) for x in segments.keys()])
print('Investigating permutations ...')
found = find_sudoku(s, elements)
if found:
    for r in found.rows:
        print ''.join(str(x) for x in r), segments[''.join(str(x) for x in r)][0]

from code import interact
interact(local=locals())
