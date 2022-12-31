l1 = [1, 4, 9, 10, 23]
l2 = [4, 9]

# method 1
for elem in l2:
    l1.remove(elem)
print(l1)

#method 2
l1 = list(set(l1)-set(l2))
print(l1)