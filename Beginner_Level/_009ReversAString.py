# Create a program to reverse a string entered by the user.

str= input("Enter a string which you want to reverse : ")



def reverseString(str):
    newStr=''
    for i in range(len(str)):
        newStr+=str[len(str)-1-i]
    
    return newStr

val=reverseString(str)
print(val)
