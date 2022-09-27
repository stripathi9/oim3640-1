# Write function(s) to repeat a simulation 10 times. In each simulation, roll 100 (6-sided) dice and print the sum.

"""
2 Functions.

Function 1. do one simulation
1. Create a variable for the sum
2. Repeat the following 100 times:
   2.1 get the random number between 1 and 6 (inclusive)
   2.2 add the random number to sum
3. print the sum


Function 2. repeat function 1 10 times
1. repeat the following 10 times:
   1.1 function1()

"""
import random


def simulate(n=100):
    """
    Simulation of rolling n dice, return the sum and the average face value
    """
    # print('Sum of the 100 dice!')  # fake it till make it
    result = 0
    for i in range(n):
        random_num = random.randint(1, 6)
        result += random_num
    return result, result / n


def repeat_simulations(m):
    """
    Repeat simulation m times.
    """
    for i in range(m):
        s, mean = simulate(100000)
        print(f'{s = }, {mean=}')


def main():
    # simulate(1000)
    repeat_simulations(5)


if __name__ == '__main__':
    main()
