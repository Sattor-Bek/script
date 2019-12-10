# def add_numbers(x,y):
#     return x+y
#
# a = add_numbers
# print a(1,2)
# print (a(1,100))
#
# def apply_twice(func, arg):
#     return func(func(arg))
#
# def add_ten(x):
#     return x + 10
#
# print(apply_twice(add_ten, 2))
#
# # How to get time of different time zone
# import datetime as dt
# import time as tm
#
# dtnow = dt.datetime.fromtimestamp(tm.time())
# dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second # get year, month, day, etc.from a datetime
# time_delta = dt.timedelta(hours = 4) #Tashkent time
# result = dtnow - time_delta
# print (result)
#
# # get user info
# class Person:
#     def set_organization(self, new_organization):
#         self.organization = new_organization
#     def set_name(self, new_name):
#         self.name = new_name
#     def set_location(self, new_location):
#         self.location = new_location

# person = Person()
# person.name = raw_input('Please input user name:')
# person.location = raw_input('Please input your address:')
# person.organization = raw_input('Please input your organization:')
# print('Name :{} Location: {} Works at: {}'.format(person.name, person.location, person.organization))

# Random id generator
# lowercase = 'abcdefghijklmnopqrstuvwxyz'
# digits = '0123456789'
# list = []
# for i in lowercase:
#     for j in lowercase:
#         for k in digits:
#             for l in digits:
#                 list.append(i+j+k+l)
#
# print len(list)
# print len([i+j+k+l for i in lowercase for j in lowercase for k in digits for l in digits])

import numpy as np

# a = np.arange(0,30,0.1) #np.arange(a, b, c) generates an array from a to b each c
# print a
# print len(a)
# a = a.reshape(5,60) #
# print a
# print len(a)

# linsp = np.linspace(0,8,9) #np.lispace(a,b,c) generates array from a to b in the range of c
# print linsp
#
# linsp.resize(3,3)
# print linsp

# a = np.random.randint(0, 9, 5)
# b = np.random.randint(0, 9, 5)
# print(a)
# print(b)
# print(np.dot(a, b))
# print(a.dot(b))
# print np.mean(a)
# print np.argmin(a)
# print np.argmax(b)

# a = np.random.randint(0, 9, (3, 2))
# b = np.random.randint(0, 9, (2, 3))
# print(a)
# print(b)
# print(np.dot(a, b))
# print(a.dot(b))

# a = np.arange(15)**5
# print [a[1], a[4], a[0:5]]

a = np.arange(36)
a.resize((6,6))
print (a)

print(a[2,3])
a2 = a[:3, :4]
print (a2)
a2[ : ] = 0

print (a)
