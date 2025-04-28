def add(a, b):
return a + b

def divide(a, b):
if b == 0:
return "Error: Cannot divide by zero"
return a / b

print("Simple calculator")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Choose the operation (1 for addition, 2 for division): ")

if op == "1":
result = add(num1, num2)
print(f "Result: {result}")
else:
print("Invalid operation")