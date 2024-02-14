from exercise2 import is_even

#def test_is_even(number):
#    """
#    Determines whether number is even or not.
#    """
#    return number % 2 == 0

def test_exercise_two():
    assert is_even(2) == True

def test_large_number():
    assert is_even(208766767909765331233498) == True

def test_odd_number():
    assert is_even(17) == False