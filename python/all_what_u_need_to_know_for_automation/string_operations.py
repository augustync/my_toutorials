#!/usr/bin/env python3

my_name = 'Augustyn Chmiel'
my_new_name = 'Auggie'
my_info = """
##############################################################
#   Master of Disaster                                       #
#   Multilane text in Python triple quotes                   #
##############################################################
"""

print(f'My name is: [{my_name}] \nMy nick name is: [{my_new_name}]\nMy Info is: [{my_info}]')

str1 = ""
str2 = " "

print(f"String 1 Empty so bool should be False [{bool(str1)}]")
print(f"String 2 with space so bool should be True : [{bool(str2)}]")

char_array = "Python 3.7"
print(f"Printing string letter per index as in array: ['P' is on 0]:[{char_array[0]}]")
print(f"Printing string letter per index as in array: ['o' is on 4]:[{char_array[4]}]")
print(f"Printing string letter per index as in array backwords: ['7' is on -1]:[{char_array[-1]}]")
print(f"Printing string letter per index as in array backwords: ['o' is on -6]:[{char_array[-6]}]")

print(f"Printing string letters from index to index [{char_array[0:6]}]")
print(f"Printing string letters from index to the end [{char_array[3:]}]")
print(f"Printing string letters from index to (-) index [{char_array[4:-2]}]")
print("We cannot change part of the string with {char_array[0]='h'}")

# delete String
del char_array
print(f"Printing char_array string after doing delete to string [NameError: name 'char_array' is not defined][char_array]")

### we can change the string to something else....
string_to_change="string will get new value ... and that is allowed"
print(string_to_change)
string_to_change = "string will get new value now!!!"
print(string_to_change)

# how to get length of the string...
string_length="string will get new value ... and that is allowed."
print(f"Getting the length of the string string_length: [{string_length}] which is length [{len(string_length)}]")

# How to add / concentate two strings
str1="First String"
str2="Adding 2nd string"
result = str1 + " " + str2
print(f"Printing str1: [{str1}] and str2: [{str2}]")
print(f"Printing result: [{result}]")

# case (Lower,Upper,tiltel etc...) conversion operations
string="My string operations Starts here with this string."
print(f"Printing string: [{string}] as it is.")
print(f"Printing string: [{string.lower()}] with all lower cases.")
print(f"Printing string: [{string.upper()}] with all upper cases.")

# to get all functions we can use with the string operations
print(f"Printing string operations: [{dir(string)}]")
print(f"Printing string operation 'swapcase' [{string.swapcase()}]")
print(f"Printing string operation 'title' [{string.title()}]")
print(f"Printing string operation 'capitalize' [{string.capitalize()}]")

# Boolean result operationson string
print("Boolean result operations on string".title())
name = "nOnus25"
print(f"Checking string name: [{name}] if starts with 'n' : [{name.startswith('n')}]")
print(f"Checking string name: [{name}] if ending with '5' : [{name.endswith('5')}]")
print(f"Checking string name: [{name}] if starts with 'no' : [{name.startswith('no')}]")
print(f"Checking string name: [{name}] if starts with 'nO' : [{name.startswith('nO')}]")
print(f"Checking string name: [{name}] if is lowercase : [{name.islower()}]")
print(f"Checking string name: [{name}] if is uppercase : [{name.isupper()}]")
print(f"Checking string name: [{name.lower()}] if is lowercase : [{name.lower().islower()}]")
print(f"Checking string name: [{name.upper()}] if is uppercase : [{name.upper().isupper()}]")
print(f"Checking string name: [{name}] if is title : [{name.istitle()}]")
print(f"Checking string name: [{name.title()}] if is title : [{name.title().istitle()}]")
print(f"Checking string name: [{name}] if is only alphabethic : [{name.isalpha()}]")
print(f"Checking string name: [{name[:-2]}] if is only alphabethic : [{name[:-2].isalpha()}]")
print(f"Checking string name: [{name}] if is only numeric : [{name.isnumeric()}]")
print(f"Checking string name: [{name[-2:]}] if is only numeric : [{name[-2:].isnumeric()}]")
print(f"To get a list of functions and descriptions for string operations:\n".title())
help(str)


# String join, center and zfill(zero fill)
print("join, center and zfill(zero fill)".title())
print(f"Print string name [{name}] with \\n join function")
print("\n".join(name))
print(f"Print string name [{name}] with \\t join function:")
print('\t'.join(name))
print(f"Print string name [{name}] with some extra str 'extra'")
print(" extra ".join(name.upper()))

print(f"Print variable [{name}] in the format centre: [{name.center(50)}]")
print(f"Print variable [{name}] in the format zfill: [{name.zfill(50)}]")
print(f"Print variable [{name}] in the format centre(30).zfill(10): [{name.center(30).zfill(10)}]")
print(f"Print variable [{name}] in the format zfill(10).centre(30): [{name.zfill(10).center(30)}]")