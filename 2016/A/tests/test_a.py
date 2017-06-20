import pytest
from A1 import solve1
from A2 import solve2, is_overlapped, combine_words

def test_solve_easy():
    s = "TEST INTE RNET PROB ROBL OBLE BLEM SOLV VING TEST"
    result = solve1(s)

    assert len(result) == 42
    for w in s.split():
        assert w in result


def check_hard(s):
    result = solve2(s)
    assert len(result) == 39
    for w in s.split():
        assert w in result

def test_solve_hard():
    check_hard("TEST INTE RNET PROB ROBL OBLE BLEM SOLV VING ENDL")
    check_hard("PPOO JJII HHHH ABBB CCDC KKKL MMNM RRQQ ABBB FFEE")

def test_is_overlapped():
    assert is_overlapped("TEST", "BLEM") == False
    assert is_overlapped("TEST", "SPOT")
    assert is_overlapped("TEST", "TEMP")
    assert is_overlapped("BAAB", "SBAA")

def test_combine_words():
    assert combine_words("TEST", "BLEM") == "TESTBLEM"
    assert combine_words("TEST", "SPOT") == "SPOTEST"
    assert combine_words("TEST", "TEMP") == "TESTEMP"
    assert combine_words("PROB", "ROBL") == "PROBL"
