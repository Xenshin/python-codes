for _ in range(int(input())):
    N = int(input())
    a = N
    while a>0:
        for i in range(1,a+1):
            if (i%5 == 0):
                print("#", end=" ")
            else:
                print("*", end=" ")
        print()        
        a -= 1