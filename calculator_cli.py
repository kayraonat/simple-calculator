def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

while True:
    print("\n --- Calculator ---")
    print("Select operation: + - * / (press q to quit)")

    choice = input("Operation: ")

    if choice == "q":
        print("Exiting...")
        break
    if choice not in ["+", "-", "*", "/"]:
        print("Invalid operation!")
        continue

    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("Error: Please enter a number!")
        continue

    if choice == "+":
        result = add(a, b)
    elif choice == "-":
        result = subtract(a, b)
    elif choice == "*":
        result = multiply(a, b)
    elif choice == "/":
        result = divide(a, b)

    print("Result:", result)