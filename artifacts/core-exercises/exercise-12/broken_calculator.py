# Broken Python Calculator
# Intentional errors for Exercise 12

def add(a, b)
    return a + b  # Missing colon on def line above

def subtract(a, b)
    return a - b

def multiply(a, b)
    return a * b

def divide(a, b)
    if b = 0:  # Should be == not =
        print("Error: Division by zero")
        return None
    return a / b

def main(
    x = 10
    y = 5
    # Missing closing parenthesis on def main( above

    print(f"Addition: {add(x, y)}")
    print(f"Subtraction: {subtract(x, y)}")
    print(f"Multiplication: {multiply(x, y)}")
    print(f"Division: {divide(x, y)}")

main()
