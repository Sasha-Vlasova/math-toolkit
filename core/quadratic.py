import cmath #note for me math is for only positive roots, but cmath can work with complex cases

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    x1 = (-b + cmath.sqrt(discriminant))/(2*a) 
    x2 = (-b - cmath.sqrt(discriminant))/(2*a)

    return x1,x2
