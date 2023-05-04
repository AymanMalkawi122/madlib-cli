
from math_series.series import sum_series
from math_series.series import fibonacci
from math_series.series import lucas

"""
sum_series test
"""


def test_sum_series_1():
    pass


def test_sum_series_2():
    assert sum_series(0, 5, 10) == 5


def test_sum_series_3():
    assert sum_series(1, 5, 10) == 10


def test_sum_series_4():
    assert sum_series(6) == 8


def test_sum_series_5():
    assert sum_series(2, 5, 10) == 15


"""
Fibonatcci test
"""


def test_fibonacci_1():
    pass


def test_fibonacci_2():
    assert fibonacci(4) == 3


def test_fibonacci_3():
    assert fibonacci(7) == 13


"""
Lucas test
"""


def test_lucas_1():
    pass


def test_lucas_2():
    assert lucas(2) == 3


def test_lucas_3():
    assert lucas(7) == 29
