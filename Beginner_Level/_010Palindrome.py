# Implement a program to check if a given string is a palindrome.
print('Welcome to pelindrome world ')
str= input("Enter a string to check  : ")


def reverseString(str):
    newStr=''
    for i in range(len(str)):
        newStr+=str[len(str)-1-i]
    
    return newStr

val=reverseString(str)

if(str==val):
    print('given string is palindrome')
else:
    print('Given string is not palindrome')