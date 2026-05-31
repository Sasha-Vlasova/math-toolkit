from quadratic import solve_quadratic

print("Quadratic Equation Solver")
print("Equation format: ax^2 + bx + c = 0")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))


result = solve_quadratic(a, b, c)

print("Solution:", result)