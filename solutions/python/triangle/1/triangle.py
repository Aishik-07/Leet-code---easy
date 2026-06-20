def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]

def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]

def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]

def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or b + c <= a or a + c <= b:
        return False
    return True