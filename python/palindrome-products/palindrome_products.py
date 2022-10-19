def smallest(max_factor, min_factor = 0) -> tuple:
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    validate(min_factor, max_factor)
    factors = range(min_factor, max_factor+1)
    _products = products(min_factor, max_factor)
    pares = palindrome_products(_products, factors)
    return pares

def largest(max_factor, min_factor=0) -> tuple:
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    validate(min_factor, max_factor)
    factors = range(min_factor, max_factor+1)
    _products = products1(min_factor, max_factor)
    pares = palindrome_products(_products, factors)
    return pares
"""
Auxiliary functions
"""
def is_palindrome(n):
    num = str(n)
    return num == num[::-1]
    
def validate(min, max):
    if min > max:
        raise ValueError("min must be <= max")

def products(min_factor, max_factor):
    return range(pow(min_factor, 2), pow(max_factor, 2) + 1)

def products1(min_factor, max_factor):
    return range(pow(max_factor, 2), pow(min_factor, 2), -1)

def palindrome_products(products, factors):
    for product in products:
        if is_palindrome(product):
            pares = []
            for factor in factors:
                j, rem = divmod(product, factor)
                if rem == 0 and j in factors:
                    pares.append([factor, j])
            if len(pares) != 0:
                return (product, pares)
    return (None, [])