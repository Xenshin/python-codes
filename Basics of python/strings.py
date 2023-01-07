for x in 'banana':
    print(x)

txt = "the best things in life are free!"
print("fri" in txt)

a = " Hello , World !   "
print(a.strip())

b = "Hello world!"
print(b.split(" "))

# Format specifier in string
age = 36
txt = "My name is Xenshin, and I am {}"
print(txt.format(age))

# escape sequence
b = "Hello\World!"
print(b)

#capitalize()
a = 'Converts the first character to upper case'
print(a.capitalize())

# casefold()
a = 'Converts String Into Lower Case'
print(a.casefold())

# center()
a = 'returns a centered string'
print(a.center(40,'*')) # first argument is the length and second is type of character

# count()
a = 'Returns the number of times a specified value occurs in a string'
print(a.count('a', 0 ,len(a))) # count(value, start, end)

# expandtabs()
txt = "H\te\tl\tl\to"
print(txt.expandtabs(8))


# join()
a = ['hello', 'this', 'is', 'an', 'example']
print('#'.join(a))

# partition()
''' It will help when you want to return the specified text and the text before and after that string'''
'''Q) return the substring before and after the specified substring'''

txt = 'before text after'
x = txt.partition('text')
print(x[0].strip(),x[2].strip()) # using tuple comprehension to get the first and last element of the string
# and using strip() function to clearoff the white spaces before and after that string

# rfind() and rindex()
''' this is used when you have to return the position of the string where it was found last'''

# reversed()
''' Reverses the sequence of a list, and print each item:'''
alph = ['a', 'b', 'c', 'd']
ralph = reversed(alph)
for i in ralph:
    print(i)

# round()
'Round a number to n decimals'
print(round(5.243568, 3)) # n = 3

# slice(n)
'''create a tuple and a slice object. Use the slice object to get only the two first items of the tuple'''
a = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
print(a[slice(4)]) # directly slicing 
u = reversed(a[slice(6)]) # to reverse
for i in u:
    print(i)
x = slice(3)
print(a[x])

# sorted()
''' sorted(iterable, reverse)
Ascending : reverse = False
Descending : reverse = True'''

a = (1, 11, 3)
print(sorted(a, reverse=True))  # Descending
print(sorted(a, reverse=False)) # Ascending

# zip()
'''returns a zip object, which is an iterator of tuples where the
first itme in each passed iterator is paired together, and then the second item 
in each passed iterator are paired together.

syntax: zip(iterator1, iterator2,....)'''
a = ("johny", "charles", "Mike")
b = ("jenny", "Christy", "Monica")
c = ("ben", "light", "milk")

x = zip(a, b,)
print(tuple(x))

