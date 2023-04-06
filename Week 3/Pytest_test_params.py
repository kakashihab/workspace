import pytest
from CalcFunctions import *

@pytest.mark.parametrize("multfirst, multsecond, multresult", [
    pytest.param(4, 6, 25, marks = pytest.mark.xfail),
    (2, 9, 18),
    (2, 8, 16),
    (3, 7, 21)])

def test_mult(multfirst, multsecond, multresult):
    obj = CalcFunctions()
    assert multresult == obj.multiply_two(multfirst, multsecond)

@pytest.mark.parametrize("cubevalue, cuberesult", [
    (2, 8),
    (3, 27),
    pytest.param(4, 65, marks = pytest.mark.xfail),
    (5, 125)])

def test_cube(cubevalue, cuberesult):
    obj = CalcFunctions()
    assert cuberesult == obj.cube(cubevalue)

@pytest.mark.parametrize("first, second, result", [
    (4, 6, 10),
    (1, 9, 10),
    (2, 8, 10),
    (3, 7, 10)])

def test_add(first, second, result):
    obj = CalcFunctions()
    assert result == obj.add_two(first, second)



