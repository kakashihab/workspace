import pytest

def test_pass1():
    assert 1 == 1

@pytest.mark.skip
def test_fail1():
    assert 1 == 2
