# BASIC CALCULATOR USING PYTHON #

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error: division by zero"
    else:
        return x / y

# Function to perform exponentiation
def exponent(x, y):
    return x ** y

# Function to perform square root
def square_root(x):
    if x < 0:
        return "Error: square root of negative number"
    else:
        return x ** 0.5


# Main program
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")
print("6. Square Root")

# Take input from the user
choice = input("Enter choice(1/2/3/4/5/6): ")
if choice>='1' and choice<='5':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        print(num1, "^", num2, "=", exponent(num1, num2))
elif choice == '6':
    num = float(input("Enter number: "))
    print("Square root of", num, "=", square_root(num))
else:
    print("Error: Please choose a valid option!")    