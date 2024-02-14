from exercise3 import biggest_prime_factor

def test_exercise_three():
    assert biggest_prime_factor(210) == 7

def test_large_number():
    assert biggest_prime_factor(2156) == 11