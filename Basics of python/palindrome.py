def palindrome(n):
    reverse = 0
    temp = n
    while (temp != 0):
        reverse = (reverse*10) + (temp%10)
        temp = int(temp/10)

    print(reverse==n)

N = int(input('enter the number to check the palindrome'))
palindrome(N)