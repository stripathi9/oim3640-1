def f(x):
    return x + 1, x * 2


# y = f(10)
# print(type(y))
# y1, y2 = f(20)
# print(y1)
# print(y2)
# print(x)


def quadratic(a, b, c):
    """
    returns something
    """
    pass
    # TODO:


# help(quadratic)
# quadratic(1, 2, 3)


def f1():

    print('Hi')  # reference: https://stackoverflow.com/a/1077349


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


def f(a, b=100):
    return a**2 + b


# print(f(2, 10))
# print(f(b=10, a=2))
# print(f(2))


def f(age):

    if age >= 6:
        print("teenager")
    elif age >= 18:
        print("adult")
    else:
        print("kid")


# f(5)


def f():
    is_name_correct = False  # flag
    while True:
        if is_name_correct is False:
            name = input("Name: ")
            if name != "peter":
                continue
            else:
                is_name_correct = True
        else:
            password = input("Password: ")
            if password == '123':
                print('Logged in!')
                break
            else:
                print('Wrong password!')


# f()

a = 200


def square(x):
    return x**2


def f():
    """sum of the squares of 1 to 3"""
    result = 0
    b = 100
    for i in range(1, 4):
        result = square(i)
        b *= i
    return result


print(f())
