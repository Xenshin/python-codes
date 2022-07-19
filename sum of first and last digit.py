# sum of the first and last digit of any integer
n = 248
last = n%10 # finding the last digit is easy
first = n # set it to n initially
while first >= 10:
    first //=10 # keep dividing by 10 untill the leftmost digit is reached
    # it will give (2)

result = first + last
print(result)