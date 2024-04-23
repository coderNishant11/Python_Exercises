# Create a program that prints the Fibonacci sequence up to a specified number of terms.

print('Welcome to the world of Fibonacci sequence')

num=int(input('Enter the number of term for fibonacci sequence : '))

def fib(n):
    a,b=0,1
    fib_seq=[]
    for i in range(n):
        fib_seq.append(a)
        a,b=b,a+b
    return fib_seq

def printFibonacciSequence(num_term):
        if(num_term<=0):
            print("Number of terms must be positive")
        

        fib_seq=fib(num_term)
        print('Fibonacci sequence upto {} term is :'.format(num_term))
        for i in fib_seq:
            print(i, end=' ')
                
printFibonacciSequence(num)
        

