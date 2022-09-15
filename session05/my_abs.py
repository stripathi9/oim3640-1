def myabs(number):
    """print the absolute value of the given number"""
    if number < 0:
        return -number
    else:
        return number


def main():
    print(myabs(-42))


if __name__ == '__main__':
    # Running as the main program ...
    # but does not execute if loaded with import ...
    main()
