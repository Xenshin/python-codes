test_list = [1, 3, 5, 6, 3, 5, 6, 1]
res = []
[res.append(x) for x in test_list if x not in res] # using list comprehension
print(res)

test_list = list(set(test_list))
print(test_list)


