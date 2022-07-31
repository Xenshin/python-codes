
lis = ['A', 'B', 'C', 'D', 'A', 'B', 'A', 'A', 'D']
new_dict = {}
for i in range(len(lis)):
    count = 1
    for j in range(len(lis)):
        if i == j:
            continue
        if lis[i] == lis[j]:
            count += 1
            new_dict[lis[i]] = count
        
for i in lis:
    if i not in new_dict:
        new_dict[i] = 1

print(new_dict)


