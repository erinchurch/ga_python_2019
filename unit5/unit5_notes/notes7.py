#modules and libaries

"""
they could come from python or htey could be from 3rd party developer

you bring those in to excute those functions in python

can inmport all

or import part of it


"""

"""

syntax  
#these always go at the top of the program
#can import many items
#usally right after the #!/user/bin...etc the very top thing, usually line 1-2
#put them in the first editable lines you have

import library #would bring in the whole thing, maybe its huge

from library import method_or_function_name

import library as perferred_name #rename it to a date that is easier for your to refer to

import pandas as pd

"""

#import datetime  #common package for data and time information
#import pandas #very common for data manipulation

#import datatime, pandas  #same as above, just in line

#from datetime import date  #brings in only that method from the library datetime

"""

import datetime

today = datetime.date.today()
print(today) #prints teh date in YYYY-MM-DD
print(today.month) #just the month in M
print(today.year) #just the year in YYYY

now = datetime.datetime.now() #this is the machine or system time, can be different machine to machine, region to region
#library.method.function()
print(now)

"""
"""
import datetime as t

today = t.date.today()
print(today)
print(today.month)
print(today.year)

now = t.datetime.now()
print(now)

"""

import datetime

time = datetime.datetime.now()


print(type(time))
#returns a class that is <class 'datetime.datetime'>

print("Weekday, short version", time.strftime("%a")) #%a is the abbreviation short form "Sat"
print("Weekday, Full version", time.strftime("%A")) #%A is the full form "Saturday

print("Weekday as a number, 0 is sunday monday-saturday is 1-6", time.strftime("%w"))


