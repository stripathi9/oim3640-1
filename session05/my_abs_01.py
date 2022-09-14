def my_abs(x):
    """
    This is our own version of abs function.

    Return the absolute value of x
    """
    # print(f'{x = }')
    if x < 0:
        return -x
    else:
        return x


a = -3

# square root of the absolute value of a

import math
res = math.sqrt(my_abs('-3'))

print(res)
# help(my_abs)

# print(x)
