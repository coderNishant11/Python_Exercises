# Implement a basic calculator program that can perform addition, subtraction, multiplication, and division.


def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def division(x,y):
    if y==0:
        return "Error! divison by zero"
    return x/y

print('Enter to the world of basic calculator.')

print('select operation')

print('1. Add')
print('2. substraction')
print('3. Multiplication')
print('4. Division')

while True:
    choice= input(' Select operation (1,2,3,4): ')

    if choice in ('1','2','3','4'):

        num1= float(input('Enter your first number : '))
        num2= float(input('Enter your second number : '))

        if choice=='1':
            print('Result : ',add(num1,num2))
        elif choice=='2':
            print('Result : ', sub(num1,num2))
        elif choice=='3':
            print('Result : ',sub(num1,num2))
        elif choice=='4':
            print('Result : ',division(num1,num2))
    else:
        print('Invalid Input')

    again = input('Do you want to calculate another calculation (yes/no): ')

    if again.lower()!='yes':
        break
