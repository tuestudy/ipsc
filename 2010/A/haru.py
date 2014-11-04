
def main():
    t = input()
    print t
    for _ in range(t):
        raw_input()
        n = input()
        ns = sorted(int(x) for x in raw_input().strip().split())
        result = []
        for i in range(n / 2):
            result.append(ns[n - 1 - i])
            result.append(ns[0 + i])
        if len(result) < n:
            result.append(ns[n / 2])
        print
        print str(n)
        print ' '.join([str(x) for x in result])

if __name__ == '__main__':
    main()
