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
y = 0

thisdict = dict.fromkeys(x,y) # this will create the dictionary with specified keys and the specified value
print(thisdict)

