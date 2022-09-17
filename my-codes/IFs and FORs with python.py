for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        if (i!=0):
            if (i%2==0):
                print(i*2)
            else:
                print(i*i)
        else:
            print(i+3)

