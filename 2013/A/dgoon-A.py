COINS = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

def coin_count(remain):
    ret = []
    for c in reversed(COINS):
        cnt = 0
        while remain >= c:
            remain -= c
            cnt += 1
        ret.append(cnt)
    assert(remain==0)
    return reversed(ret)

def solve():
    raw_input()
    e, c = map(int, raw_input().strip().split())
    remain = e*100 + c
    print ' '.join(str(x) for x in coin_count(remain))

T = input()
for _ in range(T):
    solve()
