"""
Fill missing code or correct any errors so that functions will return correct values
To check if everything is ok use pytest
pytest PythonVariableTypes/Exercises_1.py
"""


# pylint: disable-all


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
    Find
    """
    var_a = 0.1 + 0.2
    comparison_result = (var_a == 0.3)
    # Uncomment line below if you know why it is failing (ctrl + /)
    # comparison_result = True
    assert comparison_result is True


@staticmethod
def test_q6():
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


@staticmethod
def test_q7():
    """
    write a function that returns Fibonacci sequence
    """

    def Fibonacci(n):
        """
        return a list looking like [0, 1, 1, 2, 3, 5 ......]
        that has n elements
        """
        fibonnaci_numbers = []
        """
        write function here
        """
        return fibonnaci_numbers

    assert Fibonacci(3) == [0, 1, 1]
    assert Fibonacci(0) == []
    assert Fibonacci(-5) == []
    assert Fibonacci(1) == [0]
    assert Fibonacci(6) == [0, 1, 1, 2, 3, 5]
    assert len(Fibonacci(2000)) == 2000


@staticmethod
def test_q8():
    """
    write a function that returns a factorial
    """

    def Factorial(n):
        """
        return value n! for n >= 0 and None for n<0 and non-integers
        """
        Factorial = None
        """
        write function here
        """
        return Factorial

    assert Factorial(3) == 6
    assert Factorial(0) == 1
    assert Factorial(-5) is None
    assert Factorial(1) == 1
    assert Factorial(6) == 720
    assert Factorial(0.56) is None


@staticmethod
def test_q9():
    """
    write a function that replaces lowercase letters with upper case and uppercase with lowercase
    and also removes every third letter
    """

    def string_op(str_in):
        """
        replaces lowercase letters with upper case and uppercase with lowercase
        and also removes every third letter
        """
        str_out = ''
        """
        write function here
        """
        return str_out

    assert string_op("AlaMaKota") == "aLmAOT"
    assert string_op("") == ""
    assert string_op("AAAA") == "aaa"


@staticmethod
def test_ex_q9():
    """
    write a function that replaces letters cases with the same case that the first letter has
    and also removes every third letter
    This exercise will most likely require searching for help on the internet
    """

    def string_op(str_in):
        """
        replaces letters cases with the same case that the first letter has
        and also removes every third letter
        """
        str_out = ''
        """
        write function here
        """
        return str_out

    assert string_op("AlaMaKota") == "ALMAOT"
    assert string_op("") == ""
    assert string_op("Aaaa") == "AAA"
    assert string_op("conCURRENT") == "cocuret"