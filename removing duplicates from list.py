test_list = [(1,3), (7,7), (1,3), (7,8), (1,3), (7,7), (7,8), (4, 2), (7, 8), (7, 8), (4, 2), (4, 2)] 
res = []
[res.append(x) for x in test_list if x not in res] # using list comprehension
print(res)

test_list = list(set(test_list))
print(test_list)



