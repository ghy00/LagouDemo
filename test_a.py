# content of test_a.py

import pytest


def func(x):
    return x + 1


@pytest.mark.parametrize('a,b', [
    (1, 2),
    (10, 20)
])
def test_answer(a, b):
    assert func(a) == b


def test_answe1():
    assert func(4) == 5


def test_answe2():
    assert func(5) != 5


class TestDemo:
    def test_a(self):
        print("a")

    def test_b(self):
        print("b")


if __name__ == '__main__':
    pytest.main(['test_a.py::TestDemo', '-v'])
