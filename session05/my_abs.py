def myabs(number):
    """return the absolute value of the given number"""
    if number < 0:
        return -number
    else:
        return number


# print(myabs(-42))

def main():
    # all the test code should be here
    print(myabs(-42))


if __name__ == '__main__':
    # Running as the main program ...
    # but does not execute if loaded with import ...
    main()
