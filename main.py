from core.quadratic import solve_quadratic
from core.linear import solve_linear
from core.vieta import vieta_analysis

"""
#Check the water - simple functionality:
print("Quadratic Equation Solver")
print("Equation format: ax^2 + bx + c = 0")

try:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    if a == 0:
        print("Error: 'a' cannot be 0 for a quadratic equation.")
    else:
        result = solve_quadratic(a, b, c)
        print("Solution:", result)

except ValueError:
    print("Error: Please enter valid numbers only.")
"""

def menu():
    print("\nMath Toolkit")
    print("1. Solve Quadratic Equation")
    print("2. Solve Linear Equation")
    print("0. Exit")

while True:
    menu()
    choice = input("\nChoose an option: ")

    if choice == "1":
        try:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))

            if a == 0:
                print("Error: 'a' cannot be 0 for a quadratic equation.")
            else:
                result = solve_quadratic(a, b, c)
                print("Solution:", result)

        except ValueError:
            print("Error: Please enter valid numbers only.")

    elif choice == "2":
        try:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))

            result = solve_linear(a, b)
            print("Solution:", result)

            analysis = vieta_analysis(a, b, c)

            print("Vieta Analysis:")
            print("Sum of roots:", analysis["sum_of_roots"])
            print("Product of roots:", analysis["product_of_roots"])


        except ValueError:
            print("Error: Please enter valid numbers.")
    
    
    
    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")