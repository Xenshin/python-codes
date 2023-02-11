# count()
'returns the number of elements with the specified value'

# extend()
'Add the elements of a list (or any iterable), to the end of the current list'
fruits = ['apple', 'banana', 'cherry']
cars = ['ford', 'bmw', 'volvo']

fruits.extend(cars)
print(fruits)

# insert()
'Adds an element at the specified position'
fruits.insert(1, "orange") # syn: insert(position, element)
print(fruits)

# pop()
'Removes the element at the specified position'
fruits.pop(1)
print(fruits)

# Remove()
'Removes the first item with the specified value'
fruits.remove('banana')
print(fruits)

# reverse()
'Reverses the order of the list'
fruits.reverse()
print(fruits)

# sort()
'sorts the list'
print(cars)
cars.sort(reverse=False) # ascending
print(cars)

cars.sort(reverse=True) # descending
print(cars)

this_list = ['banana', 'Orange', 'Kiwi', 'cherry']
this_list.sort() # capital letters will be sorted before lower case
print(this_list)

"customizable sort function"
this_list.sort(key = str.lower)
print(this_list)

# list comprehension()
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
new_fruits_list = [x for x in fruits if x!='apple']
print(new_fruits_list)

"create list of numbers from 0 to 9"
number_list = [x for x in range(10)]
print(number_list)

"create list of numbers less than 5"
number_list_5 = [x for x in range(10) if x < 5]
print(number_list_5)

"set all the values of the list in upper case"
upper_fruits = [x.upper() for x in fruits]
print(upper_fruits)

"set all the values in the list to 'hello'"
fruits_copy = fruits.copy()
hello_list = ['hello' for x in fruits_copy]
print(hello_list)

"return orange instead of banana"
newlist = [x if x!='banana' else 'orange' for x in fruits]
print(newlist)