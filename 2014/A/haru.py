import unittest

class ATest(unittest.TestCase):
    def test_solve_1(self):
        p = 'superfastawesome'
        q = 'superfastaxesome'
        self.assertEqual(solve(p, q), '<<<<<<wesome*')

    def test_solve_2(self):
        p = 'superfastawesome'
        q = 'xuper'
        self.assertEqual(solve(p, q), '*superfastawesome*')

    def test_solve_3(self):
        p = 'superfastawesome'
        q = 'superfastawe'
        self.assertEqual(solve(p, q), 'some*')

    def test_solve_3(self):
        p = 'hqqlohbrlwwltkrsyg'
        q = 'hqqlohbrlwwltkrsyghzxbekdlsmq'
        self.assertEqual(solve(p, q), '<' * len('hzxbekdlsmq') + '*')

    def test_find_typo_1(self):
        self.assertEqual(find_typo('abcd', 'abdd'), 2)
        self.assertEqual(find_typo('abcd', 'ab'), 2)
        self.assertEqual(find_typo('ab', 'abcd'), 2)

def find_typo(p, q):
    limit = min(len(p), len(q))
    for i in range(limit):
        if p[i] != q[i]:
            return i
    return limit

def solve(p, q):
    pos = find_typo(p, q)
    a = '<' * (len(q) - pos) + p[pos:] + '*'
    b = '*' + p + '*'
    return a if len(a) < len(b) else b

def main():
    t = input()

    for _ in range(t):
        raw_input()
        p = raw_input().strip()
        q = raw_input().strip()
        print solve(p, q)

if __name__ == '__main__':
    main()
