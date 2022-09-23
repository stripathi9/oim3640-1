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
    return # don't use break/exit()/quit


# print('hi')


def f2():
    print('hi')
    # return None # did this implicitly

# result = f2()
# print(result)
# print(f2())


def f3(x):
    x = 10
    return x ** 2

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
    return a ** 2 + b

# print(f(2, 10))
# print(f(b=10, a=2)) # keyword arguments
# print(f(2)) 

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