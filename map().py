# map() function:
'Creates a map object using an existing list and a function as its parameters'
single_list = [0,1,2,3,4,5]
double_list = map(lambda n : n*2, single_list)
print(list(double_list)) # we again use list to convert the result into a list
print(single_list) # original list remains unchanged