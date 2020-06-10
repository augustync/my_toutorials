#!/usr/bin/env python3
'''
    Basics of variables and Data Types
    - Introduction to variables and print with variables
    - Data Types
    - working with multiple variable and strings in print
    - Input and Output Syntax
'''

# Variables
x = 10
y = 10.2
print(x, y)
s='String'
# to see variable types
print(type(x))
print(type(y))
print(type(s))
# removing variable from python memory
del x
'''
    Rules to define variables names:
    - it contains letters, numbers and underscores
    - it should not be keyword
    - can't contain spaces
    - it should not start with a number
    - case sensitive
'''

################################################################
#
# Data Types
#
################################################################

x = 20
print(x)
# print variable memory address
id_x = id(x)
print(f"Memory address of variable x: {id_x}")
print(type(id_x))

a = 2 + 4j
b = 3 + 5j
c = a + b
d = 6.6
e = 7
print(c)
print(type(c))
print(d + c)
print(a, type(a))
print(d, type(d))
print(e, type(e))

################################################################
#########
# Input and output
#########
################################################################

# simple calculator
a = input("Enter a number: ")
b = input("Enter b number: ")
print(f"Result of adding {a} and {b} is: {a+b}")

a = int(input("Enter a number: "))
print(f"Variable a is {type(a)} which is int")

# automatic parsing input variables
b = eval(input("Enter b number: "))
print(f"Variable b is {type(b)} which is dynamically generated")

