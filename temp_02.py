def f(x):
    """
    docstrings, just a short summary of this function

    additional information, parameter
    Return ...
    """
    # print(x)
    return x * 2, x**2, 'wilson'


# y = f(3)
# print(type(y))
# print(y)
# # print(x)
# y1, y2, y3 = y  # unpacking a tuple
# print(y1)
# print(y2)
# print(y3)


def f1():
    """
    purpose of this function
    """
    # TODO:
    pass
    return  # don't use break/exit()/quit


# print('hi')


def f2():
    print('hi')
    # return None # did this implicitly


# result = f2()
# print(result)
# print(f2())


def f3(x):
    x = 10
    return x**2


# print(f3(2))
# print(f3(34252432423532))


def f():
    """A simple recursive function"""
    print('Did you mean recursion?')

    import time

    time.sleep(1)

    f()


# f()


def f(a, b=100):
    return a**2 + b


# print(f(2, 10))
# print(f(b=10, a=2)) # keyword arguments
# print(f(2))


def f():

    bmi = 35
    if bmi <= 18.5:
        print("Underweight")
    else:
        if bmi > 18.5 and bmi <= 24.9:
            print("Normal Weight")
        else:
            if bmi > 24.9 and bmi <= 29.9:
                print("Overweight")
            else:
                print("Obesity")


def f():
    is_name_correct = False
    while True:
        if not is_name_correct:
            name = input("Name: ")
            if name != 'peter':
                continue
            else:
                is_name_correct = True
        else:
            password = input("Password: ")
            if password == '123':
                print('Thank you!')
                break
            else:
                print('Wrong password! Try again!')


# f()


import wilson


def f():
    """sum up squares of 1 to 4"""
    result = 0
    for i in range(4):
        result = wilson.square(i)
    return result


print(f())
