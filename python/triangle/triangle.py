def equilateral(sides): 
    return is_triangle(sides) and len(set(sides)) == 1

def isosceles(sides:list):
    return is_triangle(sides)  and len(set(sides)) <= 2

def scalene(sides:list):
    return is_triangle(sides) and len(set(sides)) == 3

def is_triangle(sides:list):
    sides = sorted(sides)
    return sum(sides[:2]) > sides[2]
