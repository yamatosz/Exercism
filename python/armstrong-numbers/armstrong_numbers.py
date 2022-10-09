def is_armstrong_number(number):
    numbers = [int(_number) for _number in str(number)]
    armstrong = 0
    for i in range(0, len(numbers)):
        armstrong += numbers[i]**len(numbers)

    return number == armstrong