
from math_series import sum_series
from math_series import fibonacci
from math_series import lucas

"""
sum_series test
"""


def test_fibonacci_1():
    pass


def test_fibonacci_2():
    assert sum_series(0, 5, 10) == 5


def test_fibonacci_3():
    assert sum_series(1, 5, 10) == 5


def test_fibonacci_4():
    assert sum_series(6) == 8


def test_fibonacci_5():
    assert sum_series(6, 2, 1) == 18


"""
Fibonatcci test
"""


def test_fibonacci_1():
    pass


def test_fibonacci_2():
    assert fibonacci(3) == 5


def test_fibonacci_3():
    assert fibonacci(3) == 5


"""
Lucas test
"""


def test_lucas_1():
    pass


def test_lucas_2():
    assert lucas(3) == 5


def test_lucas_3():
    assert lucas(3) == 5
