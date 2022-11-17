import math as m

def get_requirements():
    print("Python Calculator with Error Handling")
    print("\n1. Program calculates two numbers, and rounds to two decimal places.")
    print("2. Prompt user for two numbers, and a suitable operator.")
    print("3. Use Python error handling to validate data.")
    print("4. Test for correct arithmetic operator.")
    print("5. Division by zero not permitted.")
    print("6. Note: Program loops until correct input entered - numbers and arithmetic operator.")
    print("7. Replicate display below.")

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def getNum(prompt):
    while True:
        try:
            return float(input("\n" + prompt + " "))
        except ValueError:
            print("Not valid number!")

def getOp():
    validOperators = ['+', '-', '*', '/', '//', '%', '**']
    print("\nSuitable Operators: +, -, *, /, // (integer division), % (modulo operator), ** (power): ")
    while True:
        op = input("Enter operator: ")
        try:
            validOperators.index(op)
            return op
        except ValueError:
            print("\nInvalid operator! Try again!")
    
def calc():
    num1 = getNum("Enter num1: ")
    num2 = getNum("\nEnter num2: ")
    op = getOp()
    sum = 0

    if op == '+':
        sum = num1 + num2
    elif op == '-':
        sum = num1 - num2
    elif op == '*':
        sum = num1 * num2
    elif op == '**':
        sum = num1 ** num2
    elif op == '%':
        while True:
            try:
                sum = num1 % num2
                break
            except ZeroDivisionError:
                num2 = getNum("Hey! You can't divide by zero! Re-enter num2: ")

    elif op == '/':
        while True:
            try:
                sum = num1 / num2
                break 
            except ZeroDivisionError:
                num2 = getNum("Hey! You can't divide by zero! Re-enter num2: ")

    elif op == '//':
        while True:
            try:
                sum = num1 // num2
                break 
            except ZeroDivisionError:
                num2 = getNum("Hey! You can't divide by zero! Re-enter num2: ")
    
    else:
        print("Invalid operator! Try again!")
    
    print("Answer is " + str(round(sum,2)))
    print("\nThank you for using our Math Calculator!")
    print()