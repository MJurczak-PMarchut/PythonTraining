"""
Basic variable types like int, float, str
"""

"""
Operators
+ add
- substract
* multiply
/ divide
// divide without change of type
% modulo
"""

print(
    """
INT is a type that stores integer values of theoretically unlimited size
All operations on it behave as one could expect 

A = 5
B = 1456463545643565815186515151851645341566841815453145848485423457457575448484848468484848452458848477878454264732655
C = A*B
print("C =", C)

"""
)

A = 5
B = 1456463545643565815186515151851645341566841815453145848485423457457575448484848468484848452458848477878454264732655
C = A * B
print("C =", C)

print(
    """
Float is a way to store numbers that have a fraction or are a result of division that could generate it


D = B/A
print("D =", D)
print("type of D is", type(D))

"""
)

D = B / A
print("D =", D)
print("type of D is", type(D))

print(
    """
One can assign float value using a notation with a .
eg.
E = 15.
or
E = 15.0
"""
)

print(
    """
unlike ints floats have a limited max value and limited precision
so 1 is not always 1 but for example 1.0000000000000000000004
F = 1.7976931348623157e+308
print("F =", F*1.1)
"""
)

F = 1.7976931348623157e+308
print("F =", F * 1.1)
