"""
In python variables can also be array like eg. list, str, dict
Lets start with string
"""

my_str = "Python"
print(my_str)

"""
many of standard operations can be applied to it
"""

A = my_str*2
B = my_str + "ABE"

print(A)
print(B)

"""
specific letters can be extracted from it
"""

C = my_str[0]
print(C)

"""
Or ranges
"""

D = my_str[2:5]
print(D)

"""
[start:end:step] is a notation that is used to access portion of a list or string
if any value is left python will use a default value eg.
start, end and step can be any integer
"""

D = my_str[::-1]
print(D)

"""
Using an index that is out of range will cause Index Out Of Range exception to be raised
"""

D = my_str[15]