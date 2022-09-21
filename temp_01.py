def f(x):
    return x + 1, x * 2


# y = f(10)
# print(type(y))
# y1, y2 = f(20)
# print(y1)
# print(y2)
# print(x)


def quadratic(a, b,c):
    """
    returns something
    """
    pass
    # TODO: 

# help(quadratic)
# quadratic(1, 2, 3)



def f1():
    
    print('Hi') # reference: https://stackoverflow.com/a/1077349

# result = f1()
# print(result)


def f2(x):
    x = 10
    return x * 2

# print(f2(43245324))


def f():
    """
    A simple recursive function
    """
    print('Did you mean recursion?')
    import time
    time.sleep(1)
    f()


f() 