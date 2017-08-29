import pytest
from B1 import Problem

def test_problem_state_init():
    assert Problem(2, 2, 'B').path_count == 2
    assert Problem(2, 1, 'W').path_count == 1
    assert Problem(2, 1, 'B').path_count == 1
    assert Problem(3, 3, 'W').path_count == 5
    assert Problem(3, 3, 'B').path_count == 4
    assert Problem(3, 5, 'W').path_count == 8
    assert Problem(3, 5, 'B').path_count == 7
    assert Problem(5, 3, 'W').path_count == 8
    assert Problem(5, 3, 'B').path_count == 7


def test_get_next_position():
    p = Problem(3, 3, 'W')
    assert p.get_next_position([(0, 0), (1, 1)]) == (2, 0)

    p = Problem(4, 4, 'W')
    assert p.get_next_position([(0, 0), (1, 1), (2, 0), (0, 2)]) == (1, 3)

    p = Problem(4, 5, 'W')
    assert p.get_next_position([(0, 0), (1, 1), (2, 0), (0, 2), (1, 3)]) == (3, 1)

    p = Problem(4, 5, 'W')
    assert p.get_next_position([(0, 0), (1, 1), (2, 0), (0, 2), (1, 3), (3, 1)]) == (0, 4)

    p = Problem(4, 5, 'W')
    assert p.get_next_position([(0, 0), (1, 1), (2, 0), (0, 2), (1, 3), (3, 1), (0, 4)]) == (2, 2)

    p = Problem(4, 5, 'W')
    assert p.get_next_position([(0, 0), (1, 1), (2, 0), (0, 2), (1, 3), (3, 1), (0, 4), (2, 2)]) == (3, 3)

    p = Problem(4, 5, 'W')
    assert p.get_next_position([(0, 0), (1, 1), (2, 0), (0, 2), (1, 3), (3, 1), (0, 4), (2, 2), (3, 3)]) == (2, 4)

def test_path():
    assert Problem(1, 2, 'W').path() == [(0, 0)]
    assert Problem(1, 2, 'B').path() == [(0, 1)]
    assert Problem(2, 1, 'W').path() == [(0, 0)]
    assert Problem(2, 1, 'B').path() == [(1, 0)]
    assert Problem(2, 2, 'W').path() == [(0, 0), (1, 1)]
    assert Problem(2, 2, 'B').path() == [(1, 0), (0, 1)]
    assert Problem(2, 3, 'W').path() == [(0, 0), (1, 1), (0, 2)]
    assert Problem(2, 3, 'B').path() == [(1, 0), (0, 1), (1, 2)]
    assert Problem(3, 2, 'W').path() == [(0, 0), (1, 1), (2, 0)]
    assert Problem(3, 2, 'B').path() == [(0, 1), (1, 0), (2, 1)]
    assert Problem(3, 3, 'W').path() == [(0, 0), (2, 2), (1, 1), (2, 0), (0, 2)]
    assert Problem(3, 3, 'B').path() == [(1, 0), (0, 1), (1, 2), (2, 1)]
    assert Problem(4, 5, 'W').path() == [(0, 0), (1, 1), (2, 0), (0, 2), (1, 3), (3, 1), (0, 4), (2, 2), (3, 3), (2, 4)]

def test_solve_easy():
    assert Problem(2, 2, 'W').path() == [(0, 0), (1, 1)]
    assert Problem(2, 2, 'B').path() == [(1, 0), (0, 1)]
