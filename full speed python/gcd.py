def gcd(m,n):
    fm = []
    for i in range(1, m+1):
        if (m%i == 0):
            fm.append(i)
    
    fn = []
    for j in range(1, n+1):
        if (n%j == 0):
            fn.append(j)
    
    cf = []
    for i in fm:
        if i in fn:
            cf.append(i)
    
    print(cf[-1])

gcd(14, 63)


## Improved Algorithm
def gcd_1(m,n):
    cf = []
    for i in range(1, min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            cf.append(i)
    
    print(cf[-1])

gcd_1(14,63)

## Further improved algorithm
def gcd_2(m,n):
    for i in range(1, min(m,n)+1):
        if (m%i) == 0 and (n%i == 0):
            mcrf_value = i
    print(mcrf_value)

gcd_2(14,63)

## More improved algorithm
def gcd_3(m,n):
    for i in range(min(m,n), 1, -1):
        if (m%i == 0) and (n%i == 0):
            print(i)

gcd_3(14,63)

## further imprved algorithm
def gcd_4(m,n):
    i = min(m,n)
    while (i>0):
        if (m%i == 0) and (n%i == 0):
            print(i)
            break # break can be eliminated when we use return instead of print
        else:
            i -= 1

gcd_4(14, 63)
