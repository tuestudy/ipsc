T = input()
print T
for _ in range(T):
    print raw_input()
    print raw_input()
    ns = raw_input().split()
    a, b, c = sorted(ns[:3], key=int, reverse=True)
    print ' '.join([b, a, c] + ns[3:])
