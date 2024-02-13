
from exercise1 import sum_of_divisors


def test_exercise_one():
    assert sum_of_divisors(1000) == 233168

def test_small():
    assert sum_of_divisors(10) == 23

def test_medium():
    assert sum_of_divisors(100) == 2318
