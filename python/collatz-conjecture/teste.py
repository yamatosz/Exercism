from collatz_conjecture import steps

try:
    print(steps(0))
except ValueError as e:
    print(e)