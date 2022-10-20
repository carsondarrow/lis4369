def get_requirements():
    print("Python Selection Structures")
    print("Developer: Carson Darrow")
    print("\nProgram Requirements:\n"
        +"1. Use Python selection structure.\n"
        +"2. Prompt user for two numbers, and a suitable operator\n"
        +"3. Test for correct numeric operator.\n")
   
   
def python_calculator(a, b, c):
    if c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)
    elif c == '/':
        print(a/b)
    elif c == '*':
        print(a*b)
    elif c == '//':
        print(a//b)
    elif c == '%':
        print(a%b)
    elif c == '**':
        print(pow(a,b))
    else:
        print('Incorrect operator!')

def main():
    get_requirements()
    num1 = float(input('Num1: '))
    num2 = float(input('Num2: '))
    print("Suitable Operators: +,-,*,/,//(integer division),%(modulo operator),**(power)")
    op = input('Operator: ')
    python_calculator(num1, num2, op)

get_requirements()
main()