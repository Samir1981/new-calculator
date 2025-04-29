def add(a, b):
    return a + b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

print("Simple calculator")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Choose the operation (1 for addition, 2 for division): ")

    if op == "1":
        result = add(num1, num2)
        print(f"Result: {result}")
    elif op == "2":
        result = divide(num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid operation")
except ValueError:
    print("Error: Please enter valid numbers")