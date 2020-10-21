import pytest

def func(x):
    return x**2

def test_func():
    assert func(3) == 9

# run in cmd - 'pytest pytest_example.py'