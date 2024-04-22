# Write a program to check if a number is even or odd.
print('Welcome to the Even-Odd world. Provide your number to check.')
num=int(input('Enter your number here: '))

if(num%2==0):
    print('{} is Even number.'.format(num))
else:
    print('{} is Odd number.'.format(num))
