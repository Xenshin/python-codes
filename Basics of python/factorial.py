def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    if n < 0:
        return -1
    # Recursive call
    return n * factorial(n - 1)


print(factorial(5))



##########################################################################################
##########################################################################################


def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        res = 1
        for i in range(n,1,-1):
            res = res*i
    print(res)
    

n = int(input('enter the number to find the factorial'))
fact(n)



###########################################################################################
###########################################################################################

# FINDING TRAILING ZEROES IN FACTORIAL

def trailing_zero(n):
    if (n<0):
        print(-1)
    
    count = 0
    i = 5
    while (n / i >= 1):
        count += n // i
        i *= 5

    print(count)

n = int(input('enter the number'))
trailing_zero(n)