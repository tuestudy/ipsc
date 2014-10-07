import re

H_CANDY = re.compile('>o<')
V_CANDY = re.compile('vo\^')

def count_candy(p, box):
    return sum(len(p.findall(x)) for x in box)

def main():
    t = input()
    for _ in range(t):
        raw_input()

        r, c = raw_input().strip().split()
        rows = []
        cols = [''] * int(c)

        for _ in range(int(r)):
            rows.append(raw_input().strip())
            cols = map(lambda a, b: a + b, cols, rows[-1])

        print count_candy(H_CANDY, rows) + count_candy(V_CANDY, cols)

if __name__ == '__main__':
    main()
