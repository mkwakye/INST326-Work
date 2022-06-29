"""
Driver/Navigator: Michael Kwakye
Emails: mkwakye99@gmail.com
Assignment: Exercise 8
Date: 4_07_21

"""

class Pizza():

    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        if len(self.toppings)<=7:
            self.toppings.append(topping)
        else:
            print("No more than 7 toppings are allowed!")

class Topping():

    def __init__(self, name, num_pieces):
        self.name = name
        self.num_pieces = num_pieces

    def __repr__(self):
        return "{} pieces of {}".format(self.num_pieces, self.name)
