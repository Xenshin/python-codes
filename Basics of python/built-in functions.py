# abs() :- returns the absolute value of a number
print(abs(-7.25))
print(abs(3+5j))

# all() :- the function returns True if all the items in an iterable are True, otherwise it returns False
mylist = [True, True, True]
print(all(mylist))

# any() :- returns True if any item in an iterable object is True

# bin() :- returns the binary version of an object
print(bin(38))

# bool() :- returns the boolean value of a specified object:
''' The object will always return True, unless:
1) The object is empty, like [], (), {}
2) The object is False
3) The oject is 0
4) The object is None'''

# chr() :- returns the character that represents the specified unicode
print(chr(97))


# filter() :- mapping built in function
ages = [5, 12, 17, 18, 24, 32]

def myfunc(x):
    if x<18:
        return False
    else:
        return True

adults = filter(myfunc, ages)
for x in adults:
    print(x)

