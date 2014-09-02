def memoize(f):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper

@memoize
def f(s, n):
    if s < 0: return 0
    if s < 2: return 1
    return sum(f(s-i, n) for i in xrange(1, n+1)) % 1000000009

solve = lambda s: f(s,2) * f(s,4) % 1000000009

for i in range(input()):
    raw_input()
    print solve(input())
