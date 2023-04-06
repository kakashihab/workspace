from hello import *
import pytest

def test_hello1():
    res = hello("Bob")
    assert "hello Bob" == res

@pytest.mark.skip
def test_hello2():
    res = hello("Alice")
    assert "hello Alice" == res

@pytest.mark.xfail
def test_hello3():
    res = hello("Juliet")
    assert "hello Juliet" == res

@pytest.mark.parametrize("name", ["Jim", "Julie", "Jeremy", "Jeff", "Jane"])
def test_hello_parameters(name):
    res = hello(name)
    assert "hello " + name == res
