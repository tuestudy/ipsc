import pytest
from A import solve, click_world, flood, can_flood, is_whole_world_flooded

def test_solve_easy():
    assert len(solve(2, 2)) == 2
    assert len(solve(2, 3)) == 3
    assert len(solve(3, 3)) == 3
    assert len(solve(3, 4)) == 4
    assert len(solve(4, 4)) == 4
    assert len(solve(5, 6)) == 6
    assert len(solve(5, 7)) == 6
    assert len(solve(5, 8)) == 7
    assert len(solve(5, 9)) == 7
    assert len(solve(5, 10)) == 8
    assert len(solve(10, 5)) == 8

def test_click_world():
    result = click_world(2, 2, [(0, 0), (1, 1)])
    assert result == [[1, 0], [0, 1]]

def test_flood():
    result = flood([[1, 0], [0, 1]], 2, 2)
    assert result == [[1, 1], [1, 1]]
    result = flood([[1, 0, 1], [0, 0, 0], [0, 0, 0]], 3, 3)
    assert result == [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
    result = flood([[1, 0, 1], [0, 1, 0], [0, 0, 0]], 3, 3)
    assert result == [[1, 1, 1], [1, 1, 1], [0, 0, 0]]
    result = flood([[1, 0, 1], [0, 0, 0], [0, 1, 0]], 3, 3)
    assert result == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

def test_check_neighbor():
    assert can_flood([[1, 0], [0, 1]], 2, 2, (0, 1))
    assert not can_flood([[1, 0], [0, 0]], 2, 2, (0, 1))

def is_whole_world_flooded():
    world = [[1, 1], [1, 1]]
    assert is_whole_world_flooded([[1, 1], [1, 1]], 2, 2)
