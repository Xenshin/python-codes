# Lets print two elements between 1 to 100 whose sum is equal to certain number n
n = 143
for n1 in range(0,101):
    for n2 in range(0,101):
        if(n1 + n2 == n):
            print(n1,n2)