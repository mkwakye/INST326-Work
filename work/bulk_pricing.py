""" Calculate the price of an order of magnets according to a bulk
pricing scheme. """

"""
Names: Nicholas Rudiger, Michael Kwakye
Emails: nicrudiger@gmail.com, mkwakye99@gmail.com
Assignment: Exercise 2
Date: 2_16_21

"""

import sys


# replace this comment with your implementation of the get_cost() function
def get_cost(magnets):
    """
    Calculates the order cost for magnets based on values
    predetermined. Numbers given must be non-negative
    """
    cost = 0
    # if magnets within 0-49, use 0.75 to calculate
    if magnets >= 0 and magnets <= 49:
        cost = magnets * 0.75
        return cost
    # if magnets within 50-99, use 0.72 to calculate
    elif magnets >= 50 and magnets <= 99:
        cost = magnets * 0.72
        return cost
    # if magnets within 100-999, use 0.70 to calculate
    elif magnets >= 100 and magnets <= 999:
        cost = magnets * 0.70
        return cost
    # if magnets within 1000 or higher, use 0.67 to calculate
    elif magnets >= 1000:
        cost = magnets * 0.67
        return cost
    # return an error if a negative number is given
    elif magnets < 0:
        raise ValueError("You must enter non-negative value into this function")

if __name__ == "__main__":
    try:
        magnets = int(sys.argv[1])
    except IndexError:
        sys.exit("this program expects a number of magnets as a command-line"
                 " argument")
    except ValueError:
        sys.exit("could not convert " + sys.argv[1] + " into an integer")
    print(get_cost(magnets))
