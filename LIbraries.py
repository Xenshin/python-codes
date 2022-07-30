# DEFINITION:
''' The Python Standard library, PSL, is a collection of pre-defined modules, or sets of methods which help us perform
certain tasks in python'''

# IMPORTING A MODULE:
' it is done with the help of key word import'
import datetime
from enum import unique

date_today = datetime.date.today() # current date
print(date_today)

time_today = datetime.datetime.now()
print(time_today.strftime("%H:%M:%S")) # current time

# if we only want a  particular class from a module, we can use the 'from' keywork in the following format:
'Syntax- '# from module import class
from datetime import date
# now we only have the methods of the date class
date_today = date.today() # current date
print(date_today)
# These won't work
# time_today = datetime.datetime.now()
# print (time_today.strftime("%H:%M:%S"))# Current time

''' We can also give our own names to the modules that we import
by using the as keyword. Let's rename 'datetime' to dt and use it 
in program'''

import datetime as dt
date_today = dt.date.today()
print(date_today)

time_today = dt.datetime.now()
print(time_today.strftime("%H:%M:%S"))


# POPULAR MODULES:
# math:
' The math module offers a wide range of mathematical functions such as factorial, trignometric operations'

import math
fact_of_5 = math.factorial(5)
print(fact_of_5)

gcd = math.gcd(300, 90) # Greatest Common Denominator
print(gcd)

log100 = (math.log(10,100)) # logarithm of 10 to the base 100
print(log100)

# To get all math methods for complex numbers, use the cmath module instead

# HEAPQ
''' The heapq module allows us to create the heap data structure. A heap is a binary tree which always stores
a special value at the top (root). A minheap stores the smallest value at the top and a 
maxheap stores the largest value at the top.'''

'the pop method returns the value at the top of the heap.'
# python's heapq creates a minheap by default
import heapq
heap = [] # empty heap
# inserting elements in the heap
heapq.heappush(heap, 10)
heapq.heappush(heap, 70)
heapq.heappush(heap, 5)
heapq.heappush(heap, 35)
heapq.heappush(heap, 50)

# popping the smalles value
minimum = heapq.heappop(heap)
print(minimum)

# Random:
'the random module is used for generating random numbers in python.'
import random
rand_num = random.random()
print(rand_num) # random() method generates a random floating-point number between 0 and 1

rand_num_in_range = random.uniform(30,50)
print(rand_num_in_range) # uniform() method returns a floating-point number within a custom range

str_list = ['a', 'b', 'c', 'd', 'e']
random.shuffle(str_list)
print(str_list) # shuffle() method shuffles the elements of the list


my_list = [9, 8, 7]
new_list = [[x for x in[my_list]] for x in range(3)]
print (new_list)

my_list = [a for a in range(7)]
new_list = [a for a in range(10) if a in my_list and a%2==0]
print(new_list)

my_list = ['Hello', 'World', 'Educative']
temp = [a[1].upper() for a in my_list]
print(temp)

my_list = list()
my_list.append([4, [3, 2], 1])
my_list.extend([9, 10, 11])
print(my_list[0][1][1] + my_list[2])

my_list = (8, 7, 6, 5, 4, 3, 2, 1)
print(my_list[my_list.index(3)]),
print(my_list[my_list[my_list[6]-3]-6])

my_list = [11, 22, 32, 17, 7]
print(my_list.pop(-3)),
my_list.remove(my_list[0]),
print(my_list)

my_tuple = (2e-04, True, False, 18, 1.7, True)
val = 0
for a in my_tuple:
  val += int(a)
print(val)

my_dict = dict()
for i in range (3):
  for j in range(2):
    my_dict[i] = j
print(my_dict)

G = ['A', 'I', 'C', 'C', 'E', 'B', 'A', 'E', 'E', 'A', 'B', 'B', 'B'] 
print(G.unique())
