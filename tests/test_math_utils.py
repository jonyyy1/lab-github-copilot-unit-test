import pytest
from math_utils import generate_fibonacci, factorial


def test_generate_fibonacci_zero():
    assert generate_fibonacci(0) == []


def test_generate_fibonacci_one():
    assert generate_fibonacci(1) == [0]


def test_generate_fibonacci_sequence():
    assert generate_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def test_generate_fibonacci_negative():
    with pytest.raises(ValueError):
        generate_fibonacci(-5)


def test_generate_fibonacci_non_integer():
    # range() requires an integer; passing a float should raise a TypeError
    with pytest.raises(TypeError):
        generate_fibonacci(3.5)


def test_factorial_valid():
    assert factorial(5) == 120


def test_factorial_zero_and_one():
    assert factorial(0) == 1
    assert factorial(1) == 1


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-2)


def test_factorial_non_integer():
    # range() requires an integer; passing a float should raise a TypeError
    with pytest.raises(TypeError):
        factorial(2.7)
