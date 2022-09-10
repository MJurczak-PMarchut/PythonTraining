"""
This file explains basics of for loops
"""

print(
    """
    A for loop is a type of loop that is iterating over a list of values eg.

    for number in range(4):
        print(f'number is equal to: {number}')

"""
)

for number in range(4):
    print(f'number is equal to: {number}')

print(
    """
    One can also operate on string letters or elements of a list, eg.

    MY_STR = 'PythoN'

    for letter in MY_STR:
        print(f'letter is equal to: {letter}')

"""
)

MY_STR = 'PythoN'

for letter in MY_STR:
    print(f'letter is equal to: {letter}')

print(
    """
    For ease of use one can pass more variables to be iterated on using zip, eg.

    MY_STR = 'PythoN'

    for letter, index in zip(MY_STR, range(len(MY_STR))):
        print(f'letter @index={index} is equal to: {letter}')

"""
)

MY_STR = 'PythoN'

for letter, index in zip(MY_STR, range(len(MY_STR))):
    print(f'letter @index={index} is equal to: {letter}')

print(
    """
    We can use that to for example skip certain indexes

    MY_STR = 'PythoN'

    for letter, index in zip(MY_STR, range(len(MY_STR))):
        if index > 3:
            print(f'letter @index={index} is equal to: {letter}')

"""
)

MY_STR = 'PythoN'

for letter, index in zip(MY_STR, range(len(MY_STR))):
    if index > 3:
        print(f'letter @index={index} is equal to: {letter}')
