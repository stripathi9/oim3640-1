def countdown(n):
    while n > 0:  # repeat the following step(s) until n > 0 is not True
        print(n)
        n = n - 1
    print('Blastoff!')


# countdown(3)

def f():
    while True:
        message = input('Please enter a command: ')
        print(message)
        if message == 'quit':
            print('bye')
            break

# f()

# When to use for loop:
#  - when we know exactly how many times of iterations
#  - when we want to iterate over a sequence

# when to use while loop:
#  - if we only know when/what condition to stop
