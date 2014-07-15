import itertools

r, s, m = 43, 22, 2 ** 32

def memoized(f):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper

def make_prg(seeds, r, s, m):
    def c(i):
        if i >= 43 and x(i-s) - x(i-r) - c(i-1) < 0:
            return 1
        else:
            return 0

    @memoized
    def x(i):
        if i < 43:
            return seeds[i]
        return (x(i-s) - x(i-r) - c(i-1)) % m
    for i in itertools.count(43):
        yield x(i)

def test_prg():
    seeds = [999999999 * (i ** 3) % m for i in range(r)]
    rng = make_prg(seeds, r, s, m)
    assert next(rng) == 1050500563
    assert next(rng) == 4071029865
    assert next(rng) == 4242540160
    #assert next(rng) == 1565031450
    #assert next(rng) == 333471031
    #assert next(rng) == 547858901
    #assert next(rng) == 2208195061
    #assert next(rng) == 1019512215
    #assert next(rng) == 1276777658
    #assert next(rng) == 2979991393
