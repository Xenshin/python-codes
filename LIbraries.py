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