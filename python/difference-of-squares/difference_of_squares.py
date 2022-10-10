def square_of_sum(number):
    numbers = 0
    while number:
        numbers += number
        number -= 1
    return numbers**2


def sum_of_squares(number):
    numbers = 0
    while number:
        numbers += number**2
        number -= 1
    return numbers


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
