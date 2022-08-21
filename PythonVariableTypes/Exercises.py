"""
Fill missing code or correct any errors so that functions will return correct values
To check if everything is ok use pytest
pytest PythonVariableTypes/Exercises.py
"""
# pylint: disable-all


@staticmethod
def test_q1():
    """
    By filling missing code create list containing middle values from List1
    """
    list_1 = [1, 2, 3, 4]
    list_2 = list_1[""" Fill here """]
    assert list_2 == [2, 3]


@staticmethod
def test_q2():
    """
    By filling missing code reverse list defined here
    """
    list_1 = [4, 5, 6, 7, 8, 9]
    list_1 = """ Fill here """
    assert list_1 == [9, 8, 7, 6, 5, 4]


@staticmethod
def test_q3():
    """
    By filling missing code reverse list defined here and take only last 3 values of original list
    """
    list_1 = [4, 5, 6, 7, 8, 9]
    list_1 = """ Fill here """
    assert list_1 == [9, 8, 7]


@staticmethod
def test_q4():
    """
    Figure out what is wrong here (You don't have to correct it)
    """
    var_a = 0.1 + 0.2
    comparison_result = (var_a == 0.3)
    # Uncomment line below if you know why it is failing (ctrl + /)
    # comparison_result = True
    assert comparison_result is True


@staticmethod
def test_q5():
    """
    Create a class Bus that has default capacity of 50
    """

    class Vehicle:
        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage

        def seating_capacity(self):
            raise NotImplementedError

    solaris = Bus('bus', 90, 1.4)

    assert solaris.seating_capacity() == "The seating capacity of a bus is 50 passengers"
