# Create a program to calculate the sum of two numbers entered by the user.
print('Enter to addition world. Please provide two numbers which you want to add. ')
num1=int(input('Enter first number here: '))
num2=int(input('Enter second number here: '))

def addTwoNumber(num1,num2):
    sum=num1+num2
    return sum
sum= addTwoNumber(num1,num2)


print('the sum of {} and {} is {}'.format(num1,num2,sum))