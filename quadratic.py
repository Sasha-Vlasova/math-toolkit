import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant <0:
        return "No real solutions"

    x1 = (-b + math.sqrt(discriminant))/(2*a)
    x2 = (-b - math.sqrt(discriminant))/(2*a)

    return x1,x2