def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y
def power(x,caly):
     return x ** y
def square_root(x):
    if x < 0:
        return "Error: Square root of a negative number is not defined."
    return x ** 0.5
def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
def logarithm(x, base):
    import math
    if x <= 0:
        return "Error: Logarithm is not defined for non-positive numbers."
    if base <= 1:
        return "Error: Logarithm base must be greater than 1."
    return math.log(x, base)
def calculator():
    print("== Simple Calculator ==")
    print("Select Operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Logarithm")
    print("9. Exit")
    
    while True:
        choice = input("\nEnter choice (1-9): ").strip()

        if choice == '9':
            print("Exiting the calculator. Goodbye!")
            break
        elif choice in ['1', '2', '3', '4', '5','6','7','8']:
            num1 = float(input("Enter first number: "))
            if choice in ['1', '2', '3', '4', '5']:
                num2 = float(input("Enter second number: "))
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {power(num1, num2)}")
            elif choice == '6':
                print(f"Result: {square_root(num1)}")
            elif choice == '7':
                print(f"Result: {factorial(int(num1))}")
            elif choice == '8':
                base = float(input("Enter logarithm base: "))
                print(f"Result: {logarithm(num1, base)}")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    calculator()

    
    

    
