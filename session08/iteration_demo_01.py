# sum up integers from 1 to 10


def sum10():
    """sum up integers from 1 to 10"""
    result = 0

    for i in range(1, 11):
        print(f'Iteration {i}:')
        print(f'  Before adding {i}, current result is {result}.')
        result += i
        print(f'  After adding {i}, result becomes {result}.')
        print()
    return result


# print(sum10())


def sum1000():
    """return the sum of 1,..., 1000"""
    result = 0

    for i in range(1, 1001):
        print(f'Iteration {i}:')
        print(f'  Before adding {i}, current result is {result}.')
        result += i
        print(f'  After adding {i}, result becomes {result}.')
        print()
    return result


# print(sum1000())


def sum_up(n):
    """return the sum of 1,..., n"""
    result = 0

    for i in range(1, n + 1):
        # print(f'Iteration {i}:')
        # print(f'  Before adding {i}, current result is {result}.')
        result += i
        # print(f'  After adding {i}, result becomes {result}.')
        # print()
    return result


# print(sum_up(100))


def sum_up_odd(n):
    """return the sum of 1, 3, 5, n (if n is odd), n-1(if n is even)"""
    result = 0
    for i in range(1, n + 1):
        print(f'Iteration {i}:')
        if i % 2 == 1:
            print(f'  {i} is an odd number')
            result += i
            print(f'  After adding {i}, result becomes {result}.')
        print()
        # else:
        #     continue
    return result


print(sum_up_odd(10))
