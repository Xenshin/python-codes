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

