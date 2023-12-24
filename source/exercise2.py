def calculate_fibonaccis_up_to (limit):
    """
    Calculates fibonacci numbers up until a given limit.
    """
    fibonacci_numbers = [0,1]

    while True:
        next_number = fibonacci_numbers[-2] + fibonacci_numbers[-1]
        if next_number > limit:
            break
        fibonacci_numbers.append(next_number)
    return fibonacci_numbers

def is_even(number):
    """
    Determines whether number is even or not.
    """
    return number % 2 == 0

def keep_evens(list_of_numbers):
    """
    Returns a list of the even numbers within a given list.
    """
    evens = []
    for number in list_of_numbers:
        if is_even(number):
            evens.append(number)
    return evens


fibonaccis_up_to_4mill = calculate_fibonaccis_up_to(4000000)
even_fibonaccis_up_to_4mill = keep_evens(fibonaccis_up_to_4mill)
sum_of_even_4mills = sum(even_fibonaccis_up_to_4mill)
print(sum_of_even_4mills)