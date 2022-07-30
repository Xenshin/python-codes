
list1 = ['A', 'B', 'C', 'D', 'A', 'B', 'A', 'A', 'D', 4, 6, 45, 4, 5, 6]
new_dict = {}
for i in range(len(list1)):
    count = 1
    for j in range(len(list1)):
        if i == j:
            continue
        if list1[i] == list1[j]:
            count += 1
            new_dict[list1[i]] = count
        
for i in list1:
    if i not in new_dict:
        new_dict[i] = 1

print(new_dict)

