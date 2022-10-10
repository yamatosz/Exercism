def steps(number):
    if number <= 0:
        raise ValueError('Only positive integers are allowed')
    else:
        n = 0

        while number != 1:
            n+=1
            if number % 2 == 0:
                number = number/2
                continue
            number = 3*number + 1
        return n
