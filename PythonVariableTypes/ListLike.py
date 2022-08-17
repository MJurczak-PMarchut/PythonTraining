"""
Explaining array like variables
"""

print(
"""
In python variables can also be array like eg. list, str, dict
Lets start with a string

MY_STR = "Python"
print(MY_STR)

"""
)

MY_STR = "Python"
print(MY_STR)
print(
"""
many of standard operations can be applied to it
A = MY_STR * 2
B = MY_STR + "ABE"

print(A)
print(B)

"""
)

A = MY_STR * 2
B = MY_STR + "ABE"

print(A)
print(B)

print(
"""

specific letters can be extracted from it

C = MY_STR[0]
print(C)

"""
)

C = MY_STR[0]
print(C)

print(
"""
Or ranges

D = MY_STR[2:5]
print(D)

"""
)

D = MY_STR[2:5]
print(D)

print(
"""
[start:end:step] is a notation that is used to access portion of a list or string
if any value is left python will use a default value eg.
start, end and step can be any integer

D = MY_STR[::-1]
print(D)

"""
)

D = MY_STR[::-1]
print(D)

print(
"""
Using an index that is out of range will cause Index Out Of Range exception to be raised

D = MY_STR[15]

"""
)

D = MY_STR[15]
