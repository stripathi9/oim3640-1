# Exercise 3
def my_abs_3(number):
    """
    Print the absolute value of a number

    number: an integer or a floating point number
    """
    if number >= 0:
        print(number)
    else:
        print(-number)


# my_abs_3(-10)

# Exercise 4
def my_abs_4(number):
    """
    Return the absolute value of a number

    number: an integer or a floating point number
    """
    if number >= 0:
        return number
    else:
        return -number


# print(my_abs_4(-10))

# Exercise 5
def my_abs_5(number):
    """
    Return the absolute value of a number

    number: an integer or a floating point number

    pseudo-code:
    1. check the type of number
        1. if it is int or float:
            if the number is negative:
                return the opposite
        2. otherwise, raise an Error
    """
    if isinstance(number, (int, float)):
        if number >= 0:
            return number
        else:
            return -number
    else:
        print('I don\'t know how to solve this')
        # return 'Wrong type of arguments'
        raise TypeError("We do not accept this type as argument!") # a good way to handle unexpected situation


print(my_abs_5(-10))
print(my_abs_5('abc'))

print('Hi')
