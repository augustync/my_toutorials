#!/usr/bin/env python3

#    Basics of print, indentation, comments and special characters

# simple hello world script
print("Hello world!")
# old way of printing something with indent
print("Print variable align right [%20s],\nPrint variable align left [%-20s]" %("1st_var", "2nd_var"))
# new way of printing something with indentation, the new way make possible to print center alignment
print("Print variable align center [{:^20}]\nNo alignment [{}]".format("1st_var", "2nd_var"))
# other way of printing something with print function
a = 4
b = 5
r = a + b
print(f"The addition of [{a}] and [{b}] is [{r}].")

################################################################
# python indentation useage
print("this is about indentation")
if 2 < 3: #always true
    print("using indentations for if statement")
    print("comparing 2 and 3")
# end python indentation for if statement
print("end...")

################################################################
print("one line comment start with #, example below")
# one line comment
print("multiple lines comment start with ''' and ends with ''', example below:")
'''
    multiple line comment
    goes here
'''

################################################################
# special characters with print statement
# Special chars:
################
# Write special characters only inside of quotes: '' or ""
# \n - new lines
# \b - back space
# \t - new tab
# \  - escape symbol
# \a - alert sound
#################