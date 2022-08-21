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
keep in mind that value at end index will not be displayed
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

try:
    D = MY_STR[15]
except IndexError:
    print('Exception was raised')
else:
    print('Exception was not raised')
finally:
    print(f'Let\'s try with MY_STR[0]\nMY_STR[0] = {MY_STR[0]}')

print(
    """
List comprehension allows one to create a list with predetermined values quickly
Following code creates a list of numbers that are even from equation y=x**2 for x in range 0, 5

even_list  =  [x**2 for x in range(0,6) if ((x**2)%2==0)]

To take it apart:
x**2 is a x to the power of two
range(0, 6) creates a list of numbers from 0 to 5

item is added to the list if modulo 2 divison of x**2 equals 0 (number is even)



even_list = [x ** 2 for x in range(0, 6) if ((x ** 2) % 2 == 0)]
               |                               |             |
               |                               |             |
               |                               |             |
              /                                |             |
value to be --                                 |             |
added to the                                   |             |
list                                if that logic check returns true


"""
)

even_list = [x ** 2 for x in range(0, 6) if (x ** 2) % 2 == 0]
print(f'even_list = {even_list}')

print("""
lists can also be created by multiplying and adding other lists
LIST_A = 9*[0] + [1, 2, 3]

this will create a list with following values

[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]

""")

LIST_A = 9*[0] + [1, 2, 3]


print("""
************************************************************************************************************************
A dictionary is a type of collection that is ordered*, can be changed and does not allow duplicates
*since python 3.7

Dictionaries store values as key:value

It is basically a list that is indexed using keys instead of ints
Due to that access times to dictionaries are generally longer that to lists

All hashable values can be used for keys eg. int, str, float, functions

def func_a():
    pass

ex_dict = {'A': 10, 'B': "Python", 10: 'A', 3.5: 'FLOAT'}

for key in ex_dict:
    print(f'key: = {key}')
    print(f'ex_dict[key] = {ex_dict[key]}\\n')
""")


def func_a():
    pass


ex_dict = {'A': 10, 'B': "Python", 10: 'A', 31.2: 'FLOAT', func_a: 'func_a'}

for key in ex_dict:
    print(f'key: = {key}')
    print(f'ex_dict[key] = {ex_dict[key]}\n')

print('Different way to get to values')
print("""
for key, value in ex_dict.items():
    print(f'key: = {key}')
    print(f'value = {value}\n')
""")
print("***************************************************************************************************************")
for key, value in ex_dict.items():
    print(f'key: = {key}')
    print(f'value = {value}\n')

print("***************************************************************************************************************")
print("""
try:
    print(ex_dict[10.4 + 20.8])
except KeyError:
    print('Key not found!')
""")

try:
    print(ex_dict[10.4 + 20.8])
except KeyError:
    print('Key not found!')
    print(10.4 + 20.8)
