print('hello world!')
print("hello world", 50, 3.22, end=" ")#ending with end="" makes the next thing to get printed in the same line
print("printing in same line")#whatever is in between "", in end = "" gets printed in the end of the first line of the print and before the begining of the second line in the same line

#INTEGERS
print(10)
print(-3000)

#VARIABLE
num = 1234 #assigning an integer to a variable
print(num)

#FLOATING POINT NUMBERS
#floats refer to positive and negative decimal numbers
print(1.09808) #a positive float 
print(-84.649) #a negative float
flt = 24.5464 # assigning a floating point number to a variable
print(flt)

#COMPLEX NUMBERS:
"""
just like the print() statement is used to print values, 
complex() is used to create complex numbers.
It requires two values. The first one will be the real part of the comlex number, 
while the second value will be an imaginary part
"""
#complex(real, imaginary)
print(complex(10, 20)) # represents the complex number (10 +20j)
print(complex(2.5, -18.2)) # represets the complex number (2.5 -18.2j)

#BOOLEANS:
#A boolean is used to determine whether the logic of an expression or a comparison is correct. It plays a huge role in data comparison
fbool = False #assigning a boolean to a variable
print(fbool)
print(True)


#STRINGS:
"""
A string is a collection of characters closed within single, double or triple quotation marks
"""
print("hello") #double quotation marks
got = 'Game of Thrones' # single quotoation marks
print(got)
print("$") # single character
empty = ""
print(empty) #just prints an empty line
space = " " #just contains a space 
print(space, end="")
multiple_lines = '''Triple quotes allows
multi-line string'''
print(multiple_lines)

#LENGTH
print(len(multiple_lines)) #len() function indicates the number of characters in the string

#INDEXING
'''
A string in python is indexed from 0 to n-1 where n is its length. This means that the index of the first character in a string is 0
'''
#ACCESSING CHARACTERS:
'''
each character in a string can be accessed using its index. The index must be closed within square brackets, [], and 
appended to the string.
'''
batman = "Bruce Wayne"
first = batman[0] #accessing the first element
print(first)
space = batman[5] #accessing the empty space in the string
print(space)
last = batman[len(batman)-1] # accessing the last element of the string
print(last)
'''err = batman[len(batman)] #this will produce the error since the index is out of bounds
print(err)'''

#REVERSE INDEXING:
'''
we can also change our indexing convention by using negative indices.
Negative indices start from the opposite end of the string. Hence, the -1 index corresponds to the last character
'''
print(batman[-1]) #corresponds to batman[10]
print(batman[-5]) #corresponds to batman[6]

#STRING IMMUTABILITY
#once we assign a value to a string, we can't update it later. How about verifying it with an executable below?
'''
string = "Immutability"
string[0] = "O" #will give error
'''
str1 = 'hello'
print(id(str1))
str1 = 'bye'
print(id(str1))
#so remember, assigning a new value to a string variable doesn't mean that you've changed the value.

val = None
print(val) #print "None" and returns None
print(type(val))
#CHARACTERSTICS OF NONE:
'''
1.) None is not a default value for the variable that has not yet been assigned a value.
2.) None is not the same as False.
3.) None is not an empty string.
4.) None is not 0.
'''

#STRING SLICING:
'''
Slicing is the process of obtaining a portion (substring) of a string by using its indices.
'''
#syntax : string[start:end]
'''
1.) start is the index from where we want the substring to start
2.) end is the index where we want our substring to end

3.) the character at the 'end' index in the string will not be included in the substring obtained through this method
'''

mystring = "this is my string"
print(mystring[0:4])
print(mystring[1:7])
print(mystring[8:len(mystring)]) #from the 8th index till the end

#SLICING WITH A STEP:
'''
syntax: string[start:end:step]
'''

print(mystring[0:7]) #a step of 1
print(mystring[0:7:2]) #a step of 2
print(mystring[0:7:5]) #a step of 5

#REVERSE SLICING:
'''
Strings can also be sliced to return a reversed substring. In this case, we would need to switch the order of the 'start' and 'end' indices.
A negative step must also be provided:
'''

print(mystring[13:2:-1]) # take 1 step back each time
print(mystring[17:0:-2]) # take 2 step back each time

#PARTIAL SLICING:
print(mystring[:8]) # All the character before 'M'
print(mystring[8:]) # All the characters starting from 'M'
print(mystring[:]) # the whole string
print(mystring[::-1]) #the whole string in reverse (step is -1)

#STRING FORMATTING:
'''
String formatting means substituting values into a string.
1) Inserting strings within a string
2) Inserting integers within a string
3) Inserting floats within a string
'''

#inserting strings within a string
string1 = "I like %s" % "Python"
print(string1)

temp = "Educative"
string2 = "I like %s" % temp # %s is the format specifier, which tells python to insert the text here
print(string2)

string3 = "I like %s and %s" % ("python", temp)
print(string3)

#Inserting Integers within a string
my_string = "%i + %i = %i" % (1,2,3) # %i is the format specifier, which tells python to insert the integers here.
print(my_string)

#Inserting Floats within a string
string1 = "%f" % (1.11)
print(string1)

string2 = "%.2f" % (1.11) # %f is used to substitute floats within a string
print(string2)

string3 = "%.2f" % (1.117) # if we pass a float that's greater than two decimal places, then %.2f will round off the number
print(string3)

#Operators:
'''
Operators are used to perform arithmetic and logical operations on data.
They enable us to manipulate and interpret data to produce useful outputs.

5 main operator types in python are:
1) arithmetic operators
2) comparison operators
3) assignment operators
4) logical operators
5) bitwise operators
'''
#Arithmetic Operators
print(10+5) # addition
print(6-7) # subtraction
float1 = 13.65
float2 = 3.40
print(float1+float2) # addition of variables
print(float1-float2) # subtraction of variables
print(4*3) # multiplication
print(float1*float2) # multiplication of variables
print(40/10) # division
print(float1/float2) # division of variables
print(43//10) # floor division
print(float1//float2) # floor division of variables
print(10%3) # modulo (mod) 
print(float1%float2) # module of two variables


#Comparison Operators
num1 = 5
num2 = 10
num3 = 10
list1 = [6,7,8]
list2 = [6,7,8]
print(num2 > num1) # 10 is greater than 5
print(num1 > num2) # 5 is not greater than 10
print(num2 == num3) # both have the same value
print(num3 != num1) # both have different values
print(3+10 == 5+5) # both are not equal
print(3 <= 2) # 3 is not less than or equal to 2
print(num2 is num3) # both have the same object
print(list1 is not list2) # both have the different objects


#Assignment Operator
num = 10
num += 5
print(num)
num -= 5
print(num)
num *= 5
print(num)
num /= 5
print(num)
num **= 5
print(num)


#Logical Operator
my_bool = True or False # OR expression
print(my_bool)
my_bool = True and False # AND expression
print(my_bool)
my_bool = False
print(not my_bool)

# Bit Value
print( 10 * True) # Bit value of True is 1
print( 10 * False) # Bit value of False is 0

#Bitwise Operator
num1 = 10 # Binary Value = 01010
num2 = 20 # Binary value = 10100

print(num1 & num2) # 0 -> Binary value = 00000
print(num1 | num2) # 30 -> Binary value = 11110
print(num1 ^ num2) # 30 -> Binary value = 11110
print(~num1)       # -11 -> Binary value = -(1011)
print(num1 << 3)   # 80 -> Binary value = 0101 0000
print(num2 >> 3)   # 2 -> Binary value = 0010


#String Operations
#comparison operator
print('a'<'b') # 'a' has a smaller unicode value
house = "Gryffindor"
house_copy = "Gryffindor"
print(house == house_copy)
new_house = "Slytherin"
print(house == new_house)
print(new_house <= house)
print(new_house >= house)

#Concatenation
first_name = "Bat"
last_name = "man"
full_name = first_name + last_name
print(full_name)
print(full_name * 3)

#Search
# the 'in' keyword can be used to check if a particular substring exists in another string. If the substring is found, the operation returns 'True'
random_string = "this is a random string"
print('of' in random_string)
print('random' in random_string)

#CONDITIONAL STATEMENTS
# A conditional statement is a Boolean expression that, if True, executes a piece of code.
'''
There are three types of conditional statements in python:
1.) if 
2.) if-else
3.) if-elif-else
'''
# IF
num = 5
if num == 5:
    print("the number is equal to 5")

if num>5:
    print("the number is greater than 5")

# IF - Else
num = 60
output = "the number is less than or equal to 50"\
    if num <= 50 else "the number is greater than 50"

print(output)

#alternatively
if num <= 50:
    print("the number is less than or equal to 50")
else:
    print("the number is greater than 50")

# if-elif-else
num = 5
if num == 0:
    print("zero")
elif num == 1:
    print("one")
elif num == 2:
    print("two")
elif num == 3:
    print("three")
elif num == 4:
    print("four")
elif num == 5:
    print("five")
elif num == 6:
    print("six")

###########################################################   FUNCTIONS  ############################################################################################

'A function is a reusable set of operations'
# min() function:
minimun = min(10,40)
print(minimun)
minimum = min("batman", "superman") # it works with different data types
print(minimum)
minimum = min(19,34,56,42,4654) # it even works with multiple arguments
print(minimum)

'''types of functions:
1.) Built in function
2.) user defined function'''

# Syntax:
'def function_name (parameters):'

def my_print_funtion(): # No parameters
    print("this")
    print("is")
    print("A")
    print("function")
    #function ended

#calling the function in the program multiple times
my_print_funtion()
my_print_funtion()

# defining the min function
def minimum(first, second): # here we have passed the arguments in the parenthesis
    if (first < second):
        print(first)
    else:
        print(second)

minimum(45, 10)

# the 'return' statement
def minimum(first, second):
    if (first<second):
        return first
    return second

print(minimum(23, 34))

# ALTERING DATA
'''When mutable data is passed to a function, the function can modify or alter it. these modifications will stay
in effect outside the function scope as well. An example of mutable data is a list.

In the case of immutable data, the function can modify it, but the data will remain unchanged outside the function's
scope. Example of immutable data are numbers, strings, etc..'''

# mutable data
num = 20


def multiply_by_10(n):
    n *= 10
    num = n  # Changing the value inside the function
    print("Value of num inside function:", num)
    return n


multiply_by_10(num)
print("Value of num outside function:", num)  # The original value remains unchanged

# immutable data
num_list = [10, 20, 30, 40]
print(num_list)


def multiply_by_10(my_list):
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10


multiply_by_10(num_list)
print(num_list)  # The contents of the list have been changed

'Functions that are properties of a particular entity are known as methods. these methods can be accessed using the . operator'

# BUILT IN STRING FUNCTION
# Search
'find() method'
'It returns the first index at which a substring occurs in a string. If no instance of the substring is found, the method returns -1'
#syntax
'a_string.find(substring, start, end)'

random_string = "this is a string"
print(random_string.find('is'))
print(random_string.find('is',9,13)) # no instance of 'is' in this range

# replace
'the replace() method can be used to replace a part of a string with another string'
# syntax
'a_string.replace(substring_to_be_replaced, new_string)'

a_string = "welcome to Shiv Nadar University"
new_string = a_string.replace("welcome to", "Greetings from")
print(a_string)
print(new_string)

# Changing the Letter Case
print("UpperCase".upper())
print("LowerCase".lower())

# Joining Strings
my_list = ['a','b','c']
print('>>'.join(my_list)) #joining strings with >>
print('<<'.join(my_list)) #joining strings with <<
print(', '.join(my_list)) #joining strings with comma and space

# formatting
'The format() method can be used to format the specified value(s) and insert them in strings placeholder(s).'
string1 = "learn python {version} at {cname}".format(version=3, cname="github")
string2 = "learn python {0} at {1}".format(3,"github")
string3 = "learn python {} at {}".format(3, "github")

print(string1)
print(string2)
print(string3)

#LAMBDA
'A lambda is an anonymous function that returns some form of data'
'Lambdas are defined using the lambda keyword'
#syntax
'lambda parameters : expression'
triple = lambda num : num*3
print(triple(10))

concat_strings = lambda a,b,c : a[0]+b[0]+c[0] # lambda returns data, so it is a good practice to assign them to a variable
print(concat_strings("aryan", "Tiwari", "aman"))

my_func = lambda num : "high" if num > 50 else "low" # we can also use conditional statements within lambdas
print(my_func(67)) # while using conditional statement it is necessary to have if-else pair. Both cases need to be covered

# map() function:
'Creates a map object using an existing list and a function as its parameters'
single_list = [0,1,2,3,4,5]
double_list = map(lambda n : n*2, single_list)
print(list(double_list)) # we again use list to convert the result into a list
print(single_list) # original list remains unchanged

# filter() function:
'It filters out all the elements from a list if the elements satisfy the condition that is specified in the argument function'
numlist = [30,2,-15,17,9,100]
greater_than_10 = filter(lambda n : n>10, numlist)
print(list(greater_than_10))

# RECURSION:
'''It is the process in which a function calls itself during its execution. Each recursive call takes program one scope deeper
into the function.

The recursive calls stop at the BASE CASE. The base case is a check used to indicate that there should be no further recursion'''
#function which decrements a number recursively until the number becomes 0:
def rec_count(number):
    print(number)
    # base case
    if (number == 0):
        return 0
    rec_count(number - 1) # A recursive call with a different argument
    print(number)

rec_count(6) # one thing to notice is that an outer call cannot move forward until all the inner recursive calls have finished.

# LOOPS:
# A loop is a Control Structure that is used to perform a set of instructions for a specific number of times.

# For loop:
''' A for loop uses an iterator to traverse a sequence, e.g. a range of numbers, the elements of a list, etc. In simple terms,
the iterator is a variable that goes through the list.

The iterator starts from the beginning of the sequence. In each iteration, the iterator updates to the next value in the sequence.

The loop ends when the iterator reaches the end.'''

# Looping through a Range
for i in range(1,11): # A sequence from 1 to 10
    if i%2 == 0:
        print(i,"is even")
    else:
        print(i,"is odd")

# Looping through a List/String
# let's double each value in a list using a for loop
float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
print(float_list)
for i in range(0, len(float_list)):
    float_list[i] = float_list[i]*2

print(float_list)
count_greater = 0

for i in float_list:
    if i > 10:
        count_greater += 1

print(count_greater)

# Nested For Loop
# Lets print two elements between 1 to 100 whose sum is equal to certain number n
n = 143
for n1 in range(0,101):
    for n2 in range(0,101):
        if(n1 + n2 == n):
            print(n1,n2)


# The Break keyword
'''Sometimes we need to exit the loop before it reaches the end. This can happen
if we found what we were looking for and don't need to make any more computations in the loop'''

n = 143
found = False
for n1 in range(0,101):
    for n2 in range(0,101):
        if(n1+n2==n): 
            found = True
            break
    if found:
        print(n1,n2)
        break   

# The Continue keyword
'''When the continue keyword is used, the rest of that particular iteration is skipped.
The loop continues on to the next iteration. we can say that it doesn't break the loop, but 
it skips all the code in the current iteration and moves on the next one'''

num_list = list(range(0,10))

for i in num_list:
    if i == 3 or i == 6 or i == 8:
        continue # this code will skip 3, 6, and 8
    print(i) # will print all the other elements of the list

# The Pass Keyword
'''In all practical meaning, the pass statement does nothing to the code execution.
It can be used to represent an area of code that needs to be written. Hence, it is 
simply there to assist you when you haven't written a piece of code but still want
your entire program to execute.'''

num_list = list(range(0,20))

for i in num_list:
    pass # you can write code later on to use this loop

print(len(num_list))

# Finding a number
for i in range(0,10):
    if i == 89:
        print('number found') # just a random example
        break
else:
    print('number not found')


# The While loop
'The While loop keeps iterating over a certain set of operations as long as a certain condition holds True'

# Logic - While this condition is true, keep the loop running

# this finds out the maximum power of n before the value exceeds 1000
n = 2 # could be any number
power = 0
val = n
while val < 1000:
    power += 1
    val *= n
print(power)

# sum of the first and last digit of any integer
n = 248
last = n%10 # finding the last digit is easy
first = n # set it to n initially
while first >= 10:
    first //=10 # keep dividing by 10 untill the leftmost digit is reached
    # it will give (2)


# BALANCED BRACKETS EXERCISE
result = first + last
print(result)
def check_balance (my_string):
    count1 = 0 # count of '['
    count2 = 0 # count of ']'
    for i in my_string:
        if i == '[':
            count1 += 1
        if i == ']':
            count2 += 1
        
    if count1 == count2:
        return True
    else:
        return False

check_balance('[[[[][]]]]')

# SUM OF ZERO EXERCISE:

def check_sum(num_list):
    for i in range(len(num_list)):
        base = num_list[i]
        for j in range(i+1,len(num_list)):
            if (base + num_list[j] == 0):
                return True
    return False

print(check_sum([10, -14, 26, 5, -3, 13, -5]))

# FIBONACCI SERIES (LOOPS) - EXERCISE:
def fib(n):
    first = 0
    second = 1

    if n < 1:
        return -1
    if n == 1:
        return first
    if n == 2:
        return second

    count = 3 # starting from 3 because we already know the first two values
    while count <= n:
        fib_n = first + second
        first = second
        second = fib_n
        count += 1 # increment count in each iteration
    return fib_n

n = 7
print(fib(n))

# LIST:

# creating a List:
jon_snow = ["jon Snow", "winterfell", 30]
print(jon_snow)

# indexing
print(jon_snow[0])

# length
print(len(jon_snow))

# the beauty of lists lies in the fact that we are not bound to one type of data.

# lists are mutable, which further expands their functionality

print(jon_snow[2])
jon_snow[2] += 3
print(jon_snow[2])

# USING RANGE()
num_seq = range(0, 10) # a sequence from 0 tp 9
num_list = list(num_seq) # the list method casts the sequence into a list
print(num_list)

num_seq = range(3,20,3) # a sequence from 3 to 19 with a step of 3
print(list(num_seq))

# List-Ception

world_cup_winners = [[2006,"Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]

print(world_cup_winners)


# SEQUENTIAL INDEXING:
"""To access the elements of a list or a string which exists inside another list,
we can use the concept of sequential indexing."""

"""Each level of indexing takes us deeper into the list"""
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]

print(world_cup_winners[1]) 
print(world_cup_winners[1][1]) # accessing Spain
print(world_cup_winners[1][1][0]) # accessing S

# MERGING LIST
part_A = [1,2,3,4,5]
part_B = [6,7,8,9,10]
merged_list = part_A + part_B
print(merged_list)

# we can also use the extend() property of a list to add the elements of one list at the end of another
part_A.extend(part_B)
print(part_A)

# COMMON LIST OPERATIONS:

# Adding elements:
'the append() method can be used to add a new element at the end of a list'
# syntax:- a_list.append(newElement)

num_list = [] # empty list
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(num_list)