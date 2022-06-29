"""
Driver/Navigator: Michael Kwakye, Nicholas Rudiger
Emails: mkwakye99@gmail.com, nicrudiger@gmail.com
Assignment: Exercise 3
Date: 2_20_21

"""

import math
import sys

class Car:
    """
    Class Car, which contains the methods __init__(), turn(), 
    drive() & status(). These functions combine to create a 
    program that changes values of positions for cooridnates 
    based in direction (heading) and distance.
    """
    def __init__(self):
        """
        Passes a new Car object and sets different 
        default values for the attributes "x", "y" and "heading".
        """
        self.x = 0
        self.y = 0
        self.heading = "n"
        
    def turn(self, direction):
        """
        Adds one of two values to the variable named "direction"
        passed in as a parameter. The value of "heading" should 
        change to to match the value of the attribute "heading".
        """
        
        #For when the direction is equal to "r (right)"
        if (direction == "r" and self.heading == "n"):
            self.heading = "e"
        elif (direction == "r" and self.heading == "e"):
            self.heading = "s"
        elif (direction == "r" and self.heading == "s"):
            self.heading = "w"
        elif (direction == "r" and self.heading == "w"):
            self.heading = "n"
        #For when the direction is equal to "l (left)"
        elif (direction == "l" and self.heading == "n"):
            self.heading = "w"
        elif (direction == "l" and self.heading == "w"):
            self.heading = "s"
        elif (direction == "l" and self.heading == "s"):
            self.heading = "e"
        elif (direction == "l" and self.heading == "e"):
            self.heading = "n"    
        
    def drive(self, distance = 1):
        """
        This function takes in two parameters, self and distance 
        (with distance being an integer with a deafult value of 1).
        The method changes thex or y attribute depending on the
        value of the attribute "heading".
        """
        
        #Increase/decrease the value of y based on the heading direction
        if (self.heading == "n"):
            self.y += distance
        elif (self.heading == "s"):
            self.y -= distance
        #Increase/decrease the value of x based on the heading direction
        elif (self.heading == "e"):
            self.x += distance
        elif (self.heading == "w"):
            self.x -= distance
    
    def status(self):
        """
        This function takes in two parameters, self and distance 
        (with distance being an integer with a deafult value of 1).
        The method changes thex or y attribute depending on the
        value of the attribute "heading".
        """
        
        print("Coordinates: (", self.x, ", ", self.y, ")")
        print("Heading: ", self.heading)