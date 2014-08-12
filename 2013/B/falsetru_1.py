def memoized(f):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper

@memoized
def solve(x):
    if x <= 1:
        return 0
    if x % 3 == 0:
        y = x // 3
        z = y * 2
    elif x % 2 == 0:
        y = z = x // 2
    else:
        y, z = 1, x - 1
    return y * z + solve(y) + solve(z)

for c in range(input()):
    raw_input()
    n = input()
    print solve(n)
