def prime_factor_splitter(number):
    """
    Returns the smallest prime factor of a number.
    """
    for potential_prime_factor in range(2,number):
        if number % potential_prime_factor == 0:
            return potential_prime_factor
    return number

def biggest_prime_factor(number):
    """
    Returns the biggest prime factor of a number.
    """
    target = number
    while True:
        smallest_prime_factor = prime_factor_splitter(target)
        if smallest_prime_factor == target:
            return smallest_prime_factor
        else: target = target // smallest_prime_factor



print(biggest_prime_factor(600851475143))