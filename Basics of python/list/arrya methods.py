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