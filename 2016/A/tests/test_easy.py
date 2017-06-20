import pytest
from A1 import solve

def test_solve_easy():
    s = "TEST INTE RNET PROB ROBL OBLE BLEM SOLV VING TEST"
    result = solve(s)

    for w in s.split():
        assert w in result

    assert len(result) == 42 
    

