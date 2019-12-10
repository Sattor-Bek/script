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

# get user info
class Person:
    def set_organization(self, new_organization):
        self.organization = new_organization
    def set_name(self, new_name):
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location

# person = Person()
# person.name = raw_input('Please input user name:')
# person.location = raw_input('Please input your address:')
# person.organization = raw_input('Please input your organization:')
# print('Name :{} Location: {} Works at: {}'.format(person.name, person.location, person.organization))

# Random id generator
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
list = []
for i in lowercase:
    for j in lowercase:
        for k in digits:
            for l in digits:
                list.append(i+j+k+l)

print list

# answer = [i + i + j + j for i in lowercase for str(j) in digits]
# correct_answer == answer
