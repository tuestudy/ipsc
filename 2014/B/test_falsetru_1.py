from pytest import fixture

from falsetru_1 import r, s, m, make_prg, step, move, solve


@fixture(scope='function')
def dummy_rng():
    return make_prg(range(1, 44), r, s, m)

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

def test_step_left():
    assert step([2,4], 'l') == [2,4]
    assert step([2,4,8], 'l') == [2,4,8]
    assert step([2,2], 'l') == [4,0]
    assert step([2,2,0], 'l') == [4,0,0]
    assert step([2,2,4,4], 'l') == [4,8,0,0]
    assert step([0,2,2], 'l') == [4,0,0]
    assert step([2,2,4,8,0], 'l') == [4,4,8,0,0]
    assert step([0,0,0,8,8], 'l') == [16,0,0,0,0]

def test_step_right():
    assert step([2,4], 'r') == [2,4]
    assert step([0,2,2], 'r') == [0,0,4]
    assert step([4,4,8,0,0], 'r') == [0,0,0,8,8]

def test_move(dummy_rng):
    assert move([2,2,4,8,0], dummy_rng, 'l') == [4,4,8,0,2]
    assert move([4,4,8,0,2], dummy_rng, 'r') == [0,2,8,8,2]
    assert move([0,2,8,8,2], dummy_rng, 'l') == [2,16,2,0,2]

def test_solve():
    assert solve([2,4], dummy_rng(), 'lrl') == [2,4]
    assert solve([2,2,4,8,0], dummy_rng(), 'lrl') == [2,16,2,0,2]
    rng = make_prg(range(43,0,-1), r, s, m)
    assert solve([2,2,4,8,0], rng, 'lrl') == [2,16,2,2,0]
