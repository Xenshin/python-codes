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


#keys() method
x = car.keys() # returns a list containing the dictionary's keys

car["color"] = "white"
print(x)


# pop() method
x = car.pop("model", "C series") #removes the element with specified key and returns its value
print(x)

# popitem() method
car.popitem() # removes the last inserted key-value pair

