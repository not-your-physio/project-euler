
def does_divide_by_3_or_5(number):
    """
    Checks whether the number divides by 3 or 5.
    """
    if number % 5 == 0 or number % 3 == 0:
        return True
    else: return False

totalnumber = 0

for number in range(0, 1000):
    if does_divide_by_3_or_5(number):
        totalnumber += number

print(totalnumber)