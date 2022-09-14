# r1 = 1
# r2 = 10
# r3 = 2022

# area1 = 3.14 * r1 * r1
# area2 = 3.14 * r2 * r2
# area3 = 3.14 * r3 * r3

# print(area1, area2, area3)


def area_of_circle(radius): # radius is called paremeter variable
    """
    (this is docstring)
    print the area of circle, given radius
    """
    # if the function does not return
    # anything explicitly, it will return None
    # return None
    pi = 3.14157
    area = pi * radius * radius
    print(f'The area of circle with {radius=} is {area}.')
    # return area # now it is returning a value explicitly


# area_of_circle(1.0)

area1 = area_of_circle(1.0)  # the function is called/invoked, 1.0 is called argument
area2 = area_of_circle(10)
area3 = area_of_circle(2022)
print(area1, area2, area3)


def give_me_a_break():
    str1 = 'break'
    return str1
    print('another break')
    
print(give_me_a_break())