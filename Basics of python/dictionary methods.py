# clear() method:
car = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}

print(car)
car.clear()
print(car)


# fromkeys() method:
x = ('key1', 'key2', 'key3')
y = (2,3,4) # y will be assignes as a whole to all the keys

thisdict = dict.fromkeys(x,y) # this will create the dictionary with specified keys and the specified value
print(thisdict)


# get() method
'this returns the value of the item with the specified key'
car = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
x = car.get("model", 15000) # the later argument is to return the default specified value if the value of an item does not exist
print(x)


# items() method
print(car.items()) # returns a list containing a tuple for each key value pair
