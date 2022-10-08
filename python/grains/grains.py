def square(number=None):
    if number != None:
        if number < 1 or  number > 64:
            raise ValueError('square must be between 1 and 64')
        else:
            return 2 ** (number - 1)
    else:
        return 2 ** 64 - 1

def total():
    return square()