a = N
while a>0:
    for i in range(N+1):
        if i == 0:
            break
        elif (i%5 == 0):
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()        
    a -= 1
    N-=1