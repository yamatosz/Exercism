from grains import square, total

try:
    print(square(64))
    print(total())
except ValueError as e:
    print(e)