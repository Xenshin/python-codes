for i in range(1,11): # A sequence from 1 to 10
    if i%2 == 0:
        print(i,"is even")
    else:
        print(i,"is odd")

# Only even
for i in range(2,11):
    if i%2 == 0: # Replace == by != to get odd numbers
        print(i," is even")
    continue    