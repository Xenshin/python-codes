# fibonacce sequence:
'its a sequence where every number is the sum of the two numbers before it. The first two terms in the series are 0 and 1'
def fib(n):
    #the base cases
    if n<=1: # first number in the sequence
        return 0
    elif n==2: #second number in the sequence
        return 1
    else:
        #recursive call
        return fib(n-1) + fib(n-2)

print(fib(6))




#######################################################################################
#######################################################################################


def fibonacci(N):
    a, b = 0, 1
    for i in range(N):
        print(a)
        a, b = b, a+b

n =  int(input("enter the number till which you want fibonacci sequence"))
fibonacci(n)