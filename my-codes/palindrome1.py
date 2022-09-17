for _ in range(int(input())):
    str = input()
    rev_str = str[::-1]
    if str.lower() == rev_str.lower():
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

