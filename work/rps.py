"""
Names: Nicholas Rudiger, Michael Kwakye
Emails: nicrudiger@gmail.com, mkwakye99@gmail.com
Assignment: Exercise 1
Date: 1_29_21

"""

import math
import sys

another_round = "y"
while True:
    answer1 = input("Player 1: Enter your hand shape (r, p or s) ")
    answer2 = input("Player 2: Enter your hand shape (r, p or s) ")
    print("Player 1 wins!"  
              if (answer1 == "r" and answer2 == "s"
              or answer1 == "p" and answer2 == "r"
              or answer1 == "s" and answer2 == "p") else
          "Player 2 wins!"  
              if (answer2 == "r" and answer1 == "s"
              or answer2 == "p" and answer1 == "r"
              or answer2 == "s" and answer1 == "p") else
          "Tie!")
    
    #Alternative Code
    """if answer1 == answer2:
        print("Tie!")
    elif (answer1 == "r" and answer2 == "s" or 
          answer1 == "p" and answer2 == "r" or 
          answer1 == "s" and answer2 == "p"):
        print("Player 1 wins!")
    elif (answer2 == "r" and answer1 == "s" or 
          answer2 == "p" and answer1 == "r" or 
          answer2 == "s" and answer1 == "p"):
        print("Player 2 wins!")"""
        
    another_round = input("Do you want to play around round (y or n)? ")
    
    if another_round == "n":
        break
print("Goodbye!")