import pytest
from series import fibonacci
from series import lucas
from series import sum_series

def test_fib_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fib_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fib_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_fib_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_luc_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_luc_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_luc_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_luc_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_luc_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_luc_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_sum_fib_zero():
    actual = sum_series(7, 0, 1)
    expected = 13
    assert actual == expected


def test_sum_luc_zero():
    actual = sum_series(7, 2, 1)
    expected = 29
    assert actual == expected