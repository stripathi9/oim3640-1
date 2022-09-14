def my_abs(x):
    """
    This is our own version of abs function.

    print the absolute value of x
    """
    if x < 0:
        print(-x)
    else:
        print(x)


# call the function accordingly
y = -100
# calculate the square root of absolute value of y
# print(my_abs(y) ** .5)

# print(my_abs(-100))
# my_abs(0)
# my_abs(100)


def my_abs_4(x):
    """
    This is our own version of abs function.

    Return the absolute value of x
    """
    if x < 0:
        return -x
    else:
        return x


# call the function accordingly
# print(my_abs_4(-100))
# my_abs_4(0)
# my_abs_4(100)

y = -4
# calculate the square root of absolute value of y

print(my_abs_4(y) ** 0.5)
