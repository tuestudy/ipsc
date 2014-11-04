T = int(input())
print(T)
for _ in range(T):
    input()
    print()
    N = int(input())
    print(N)
    Ns = list(map(int, input().strip().split()))
    head = Ns[:3]
    sorted_head = sorted(head)
    print(' '.join(map(str, [sorted_head[1], sorted_head[0], sorted_head[2]] + Ns[3:])))
