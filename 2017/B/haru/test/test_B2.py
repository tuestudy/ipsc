import pytest
from B2 import solve, solve_odd_square_black, solve_odd_black

def test_solve_white():
    color = 'W'
    # rows = 1
    assert solve(1, 2, color) == [(0, 0)]
    assert solve(1, 3, color) == []
    assert solve(1, 4, color) == []
    # rows = 2
    assert solve(2, 2, color) == [(0, 0), (1, 1)]
    assert solve(2, 3, color) == [(0, 0), (1, 1), (0, 2)]
    assert solve(2, 4, color) == [(0, 0), (1, 1), (0, 2), (1, 3)]
    assert solve(2, 5, color) == [(0, 0), (1, 1), (0, 2), (1, 3), (0, 4)]
    assert solve(5, 2, color) == [(0, 0), (1, 1), (2, 0), (3, 1), (4, 0)]
    # else ... all case is impossible
    assert solve(3, 3, color) == []
    assert solve(3, 4, color) == []
    assert solve(5, 4, color) == []

def test_solve_black():
    color = 'B'
    # rows = 1
    assert solve(1, 2, color) == [(0, 1)]
    assert solve(1, 3, color) == [(0, 1)]
    assert solve(1, 4, color) == []
    # rows = 2
    assert solve(2, 2, color) == [(1, 0), (0, 1)]
    assert solve(2, 3, color) == [(1, 0), (0, 1), (1, 2)]
    assert solve(2, 4, color) == [(1, 0), (0, 1), (1, 2), (0, 3)]
    assert solve(2, 5, color) == [(1, 0), (0, 1), (1, 2), (0, 3), (1, 4)]
    assert solve(5, 2, color) == [(0, 1), (1, 0), (2, 1), (3, 0), (4, 1)]
    # rows and cols are same and they are odd number
    assert solve(3, 3, color) == [(1, 0), (0, 1), (1, 2), (2, 1)]
    assert len(solve(5, 5, color)) == 12
    # else ... all case is impossible
    assert solve(4, 4, color) == []
    assert solve(3, 4, color) == []
    assert solve(5, 4, color) == []

def test_solve_odd_square_black():
    assert solve_odd_square_black(3) == [(1, 0), (0, 1), (1, 2), (2, 1)]
    assert solve_odd_square_black(5) == [(1, 0), (0, 1), (1, 2), (0, 3),
        (1, 4), (2, 3), (3, 4), (4, 3),
        (3, 2), (4, 1), (3, 0), (2, 1)]
    assert len(solve_odd_square_black(7)) == 24
    assert len(solve_odd_square_black(9)) == 40
    assert len(solve_odd_square_black(11)) == 60

def test_solve_odd_black():
    assert solve_odd_black(3, 5) == [(0, 1), (1, 0), (2, 1), (1, 2), (2, 3), (1, 4), (0, 3)]
    assert solve_odd_black(5, 7) == [
        # move bottom
        (0, 1), (1, 0), (2, 1), (3, 0), (4, 1),
        # move right
        (3, 2), (4, 3), (3, 4), (4, 5),
        # move top
        (3, 6), (2, 5), (1, 6),
        # move left
        (0, 5), (1, 4), (0, 3),
        # move bottom
        (1, 2), (2, 3)]
