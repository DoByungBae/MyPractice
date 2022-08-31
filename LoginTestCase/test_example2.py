import pytest

def test_answer1():
    assert 1

@pytest.mark.unit
def test_answer0():
    assert 0

@pytest.mark.unit
def answer_true():
    assert True