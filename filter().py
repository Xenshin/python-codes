# filter() function:
'It filters out all the elements from a list if the elements satisfy the condition that is specified in the argument function'
numlist = [30,2,-15,17,9,100]
greater_than_10 = filter(lambda n : n>10, numlist)
print(list(greater_than_10))

