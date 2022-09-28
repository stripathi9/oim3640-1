# Write function(s) to repeat a simulation 10 times. In each simulation, roll 100 dice and print the sum of all the face values.


"""
I will create 2 functions.

Function 1: one simulation
1. create a variable to store the sum, and initialize to 0
2. repeat the following steps 100 times:
   2.1. get random integer between 1 and 6 (inclusive)
   2.2. add the random integer to sum variable
3. print the result

Function 2: repeat simulation 10 times
1. repeat the following 10 times:
   1.1 call function 1
"""

import random


def simulate(n=100):
    """
    roll n dice, and return the sum, average
    """
    # print('We found sum!') # fake it till make it.
    result = 0
    for i in range(n):
        random_number = random.randint(1, 6)
        result += random_number
    avg = result / n
    return result, avg


def repeat_simulation(m):
    """
    repeat the simulation m times
    """
    for i in range(m):
        s, mean = simulate(1_000_000)
        print(f'{s = }, {mean = }')


def main():
    # simulate()
    repeat_simulation(5)


if __name__ == "__main__":
    main()
