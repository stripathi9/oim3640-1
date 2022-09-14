# r1 = 1
# r2 = 10
# r3 = 2022

# area1 = 3.14 * r1 * r1
# area2 = 3.14 * r2 * r2
# area3 = 3.14 * r3 * r3

# print(area1, area2, area3)


def compute_area(radius):  # radius is the parameter variable
    """
    This is docstring which is a short description of this function

    Return the area of a circle, given radius
    """
    pi = 3.14
    area = pi * radius * radius
    # we always assume the parameter variables' values are given
    return area
    # if the function does not explicitly return any value, it will return None


area1 = compute_area(1.0)
# 1.0 is called argument, which is provided to the function call
print(area1)
# area2 = compute_area(10)
# print(area2)


import math

y = math.sqrt(area1)
print(y)


def give_me_a_break():
    str1 = 'break'
    return str1 # return always terminates the function
    print('another break')
    
print(give_me_a_break())