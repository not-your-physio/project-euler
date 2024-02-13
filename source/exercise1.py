
def does_divide_by_3_or_5(number):
    """
    Checks whether the number divides by 3 or 5.
    """
    if number % 5 == 0 or number % 3 == 0:
        return True
    else: return False

def sum_of_divisors(number):
    total = 0

    for current in range(0, number):
        if does_divide_by_3_or_5(current):
            total += current

    return total