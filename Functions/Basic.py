"""
File that explains basics of functions in python
"""

var_1 = 5


def function_1(a, b):
    """
    :param a: number
    :param b: number
    :return: a to the power of b
    """
    return a ** b


def function_2(*items):
    """
    sums up all the items
    :param items:
    :return:
    """
    sum_p = 0
    for item in items:
        sum_p = sum_p + item
    return sum_p


def function_3(**kwargs):
    """
    sums up all the items
    :param kwargs:
    :return:
    """
    for number, arg in zip(range(len(kwargs.keys())), kwargs):
        if number == 0:
            sum_p = kwargs[arg]
        else:
            sum_p += kwargs[arg]
    return sum_p


def function_4(**kwargs):
    """
    sums up all the items
    :param kwargs:
    :return:
    """
    sum_p = None
    for arg in kwargs:
        if sum_p is None:
            sum_p = kwargs[arg]
        else:
            sum_p += kwargs[arg]
    return sum_p


def function_5(a, b, operation=None):
    """
    performs operation on a and b
    :return: a operation b
    """
    if operation is not None:
        return eval(''.join([str(a), operation, str(b)]))
    return None


def function_6(a, b, c=10, *args, **kwargs):
    """
    What do I do?
    """
    if len(args):
        sum_p = args[0]
        for arg in args[1:]:
            sum_p += arg
    else:
        sum_p = 0
    if 'return_default' in kwargs:
        sum_p = kwargs['return_default']
        sum_p += sum_p
    else:
        return (a * b) + c + var_1 + sum_p


if __name__ == '__main__':
    print(f'0 to the power of 4 is: {function_1(0, 4)}')
    print(f'1 plus 4 is: {function_2(1, 4)}')
    print(f'2 plus 2 plus 45 is: {function_2(2, 2, 45)}')
    print(f'3 plus 8 plus 45 is: {function_3(a=3, b=8, c=45)}')
    print(f'4 plus 10 is: {function_5(a=4, b=10, operation="+")}')
    print(f'function_6 return is: {function_6(40, 10, 5, 10, operation="+")}')
    print(f'second function_6 return is: {function_6(40, 10, 5, 10, return_default="+")}')
