def sum10():
    """return sum of 1, 2, ..., 10"""
    result = 0

    for i in range(1, 11):
        print(f'Iteration {i}:')
        print(f'  Before adding {i}, result is {result}.')

        result += i

        print(f'  After adding {i}, result becomes {result}.\n')

    return result


# print(sum10())


def sum1000():
    """return sum of 1, 2, ..., 1000"""
    result = 0
    for i in range(1, 1001):
        # print(f'Iteration {i}:')
        # print(f'  Before adding {i}, result is {result}.')
        result += i
        # print(f'  After adding {i}, result becomes {result}.\n')
    return result


# print(sum1000())


def sum_up(n):
    """return sum of 1, 2, ..., n"""
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


# print(sum_up(1000))


def sum_up_odd(n):
    """reutrn sum of 1, 3, 5, ..., n (if n is odd), n-1 (if n is even)"""
    result = 0
    for i in range(1, n + 1):
        print(f'Iteration {i}:')
        if i % 2 == 1:  # i is odd number
            print(f' {i} is an odd number')
            result += i
            print(f' After adding {i}, result becomes {result}.')
        print()

    return result

print(sum_up_odd(10))