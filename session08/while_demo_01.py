def countdown(n):
    """"""
    # repeat the following task(s) until n > 0 is not True
    #    print n
    #    decrease n by 1
    # when n is not > 0:
    #   print Blast off!
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')


countdown(5)

"""
When to use for loop:
    - when we know exactly how many times of iteration
    - when we iterate over a sequence

When to use while loop:
    - if we only know when/ what condition to stop
"""