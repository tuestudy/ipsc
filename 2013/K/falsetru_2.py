def memoize(f):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper

@memoize
def f(n):
    if n < 0: return 0
    if n == 0: return 1
    return (f(n-1) + 2 * f(n-2) + 3 * f(n-3) + 5 * f(n-4)) % 1000000009

for i in range(input()):
    raw_input()
    print f(input())
