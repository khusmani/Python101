# https://www.edureka.co/blog/python-tutorial/#introductiontopython
print("hello world")

# String
S = "Sample String"
print(S[::-1])
print(S[3:5])
print(S.upper())
print(S.index("Str"))

# List
classes = ['Maths', 'English', 'History', 'Biology']
print(classes[0])
print(len(classes))

# remove duplicates in list
Mylist = [1, 2, 3, 2, 3, 1, 3, 1]
b = list(dict.fromkeys(Mylist))
print(b)

# set
set_name = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3, 3, 4, 5}
print(set_name)
print(set_2)

# Union of sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)

# Difference of sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A - B)

# Dict
Dict = {'Name': 'Saurabh', 'Age': 23}
Dict['Age'] = 32
Dict['Address'] = 'Starc Tower'
print(Dict['Name'])
print(Dict['Age'])
print(Dict['Address'])

# membership operator (in/not in)
X = [1, 2, 3, 4]
A = 3
print(A in X)
print(A not in X)

# if block and math operators
# if condition1:
#     statements
# elif condition2:
#     statements
# else:
#     statements
a = 21
b = 10
c = 0

if (a == b):
    print("a is equal to b")
else:
    print("a is not equal to b")

if (a != b):
    print("a is not equal to b")
else:
    print("a is equal to b")

if (a < b):
    print("a is less than b")
else:
    print("a is not less than b")
if (a > b):
    print("a is greater than b")
else:
    print("a is not greater than b")

# Loops in Python
# In Python, there are three loops:
#
# - While
# - For
# - Nested

# While loop
count = 0
while (count < 10):
    print(count)
    count = count + 1

print("Good bye While loop!")

# For loop
fruits = ['Banana', 'Apple', 'Grapes']
for index in range(len(fruits)):
    print(fruits[index])
print("Good bye For loop!")

# Nested Loop
count = 1
for i in range(10):
    print(str(i) * i)

    for j in range(0, i):
        count = count + 1
print("Good bye Nested loop!")

# Files
import os

fd = "GFG.txt"

# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello1")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

# popen() provides a pipe/gateway and accesses the file directly
#file = os.popen(fd, 'w')
#file.write("Hello2")
#file.close()
# File not closed, shown in the next function.

import math
print(math.pi)
#it will print the value of pi

import random
print(random.random())

import datetime
print(datetime.datetime.now())
#it will print the current date and time

#class
class employee:
    pass
# no attributes and methods
emp_1 = employee()
emp_2 = employee()
# instance variable can be created manually
emp_1.first = 'aayushi'
emp_1.last = 'Johari'
emp_1.email = 'aayushi@edureka.co'
emp_1.pay = 10000


emp_2.first = 'test'
emp_2.last = 'abc'
emp_2.email = 'test@company.com'
emp_2.pay = 10000
print(emp_1.email)
print(emp_2.email)

#Inheritance
class employee2:
    num_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, sal):
        self.first = first
        self.last = last
        self.sal = sal
        self.email = first + '.' + last + '@company.com'
        employee2.num_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.sal = int(self.sal * raise_amount)


class developer(employee2):
    pass


emp_1 = developer('aayushi', 'johari', 1000000)
print(emp_1.email)