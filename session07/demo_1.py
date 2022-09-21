age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')


print()

def countdown(n):
    """
    Recursive function, but not recommende to beginners
    """
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        import time
        time.sleep(1)
        countdown(n-1)

countdown(5)