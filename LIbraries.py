# DEFINITION:
''' The Python Standard library, PSL, is a collection of pre-defined modules, or sets of methods which help us perform
certain tasks in python'''

# IMPORTING A MODULE:
' it is done with the help of key word import'
import datetime

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

