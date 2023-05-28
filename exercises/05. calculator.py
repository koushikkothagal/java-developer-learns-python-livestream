# Exercise 5: Simple Calculator

# Write a Python program to create a simple calculator. The calculator should be able to perform basic operations like addition, subtraction, multiplication, and division.

# Steps:

# The program should ask the user to select an operation (either addition, subtraction, multiplication, or division).
# The program should then ask the user to input two numbers.
# The program should perform the selected operation on the two numbers and print the result.

while True:
    operation = ''
    while (operation not in ['1', '2', '3', '4', '5']):
        print(
        """Select operation:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Quit
        """)
        operation = input()
    if (operation == '5'):
        break

    operations_lambdas = {
        '1': lambda x, y: x + y,
        '2': lambda x, y: x - y,
        '3': lambda x, y: x * y,
        '4': lambda x, y: x / y,
    }

    num1 = ' '
    while (not num1.isnumeric()):
        print('Enter first number:')
        num1 = input()

    num2 = ' '
    while (not num2.isnumeric()):
        print('Enter second number:')
        num2 = input()

    print('The result is: ')
    print(operations_lambdas[operation](int(num1), int(num2)))
