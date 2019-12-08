def add_numbers(x,y):
    return x+y

a = add_numbers
print a(1,2)
print (a(1,100))

def apply_twice(func, arg):
    return func(func(arg))

def add_ten(x):
    return x + 10

print(apply_twice(add_ten, 2))

# How to get time of different time zone
import datetime as dt
import time as tm

dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second # get year, month, day, etc.from a datetime
time_delta = dt.timedelta(hours = 4) #Tashkent time
result = dtnow - time_delta
print (result)
