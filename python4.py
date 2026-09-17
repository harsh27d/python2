def add(a,b):
 return a + b
def sub(a,b):
 return a - b
def mul(a,b):
 return a * b
def div(a,b):
 return a / b
num1 =int(input("Enter first number: "))
num2 =int(input("Enter second number: "))
print("Addition:",add(num1,num2))
print("Subtraction:",sub(num1,num2))
print("Multiplication:",mul(num1,num2))
print("Division:",div(num1,num2))
choice = int(input("Enter your choice"))
match choice:
    case 1:
        print("Addition:",add(num1,num2))
    case 2:
        print("Subtraction:",sub(num1,num2))
    case 3:
        print("Multiplication:",mul(num1,num2))
    case 4:
        print("Division:",div(num1,num2))
    case _:
        print("Invalid choice")