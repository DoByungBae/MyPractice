import pytest

def inc(x):
    return x + 1

@pytest.mark.smoke
def test_answer():
    assert inc(3) == 5
