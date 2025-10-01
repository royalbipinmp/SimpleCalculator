# Simple Calculator (CLI) with loop and break

print("Welcome to CLI Calculator")

while True:
    # taking input
    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # calculation using if-else
    if op == "+":
        print("Result:", num1 + num2)
        break
    elif op == "-":
        print("Result:", num1 - num2)
        break
    elif op == "*":
        print("Result:", num1 * num2)
        break
    elif op == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
            break
        else:
            print("Error: Division by zero not allowed.")
            break
    else:
        print("Invalid operation.")
        break