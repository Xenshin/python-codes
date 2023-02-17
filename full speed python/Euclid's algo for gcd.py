def gcd(m,n):
    # assume m>=n
    if m<n:
        (m,n) = (n,m)
    
    if (m%n) == 0:
        print(n)
    else:
        diff = m-n
        # diff > n ? Possible!
        print(gcd(max(n,diff), min(n,diff))) # recursive part

gcd(14, 63)

###
###
# replacing the recursion with while loop
def gcd_1(m,n):
    if m<n:
        (m,n) = (n,m)
    
    while (m%n) != 0:
        diff = m-n
        (m,n) = (max(n,diff), min(n,diff))
    
    print(n)

gcd_1(14,63)

## even beter
def gcd_2(m,n):
    if m<n:
        (m,n) = (n,m)

    if (m%n) == 0:
        print(n)
    else:
        print(gcd(n, m%n)) # m%n < n, always