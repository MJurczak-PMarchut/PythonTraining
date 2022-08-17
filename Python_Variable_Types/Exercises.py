"""
Fill missing code or correct any errors so that functions will return correct values
To check if everything is ok use pytest
pytest Python_Variable_Types/Exercises.py
"""


@staticmethod
def test_Q1():
    """
    By filling missing code create list containing middle values from List1
    """
    List1 = [1, 2, 3, 4]
    List2 = List1[""" Fill here """]
    assert List2 == [2, 3]


@staticmethod
def test_Q2():
    """
    By filling missing code reverse list defined here
    """
    List1 = [4, 5, 6, 7, 8, 9]
    List1 = """ Fill here """
    assert List1 == [9, 8, 7, 6, 5, 4]


@staticmethod
def test_Q3():
    """
    By filling missing code reverse list defined here and take only last 3 values of original list
    """
    List1 = [4, 5, 6, 7, 8, 9]
    List1 = """ Fill here """
    assert List1 == [9, 8, 7]


@staticmethod
def test_Q4():
    """
    Figure out what is wrong here (You don't have to correct it)
    """
    A = 0.1 + 0.2
    comparison_result = (A == 0.3)
    # Uncomment line below if you know why it is failing (ctrl + /)
    # comparison_result = True
    assert comparison_result == True

