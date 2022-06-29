""" A program which play a game based on the monty hall problem"""

"""
Driver/Navigator: Michael Kwakye
Email: mkwakye99@gmail.com
Assignment: HW4
Date: 5_11_21
"""
import random

class Simulation:
    """
    Agrs:
            doornum (int): Represents number of doors
            
    This class takes in an attribute called numdoors, which is an integer
    representing the amount of doors that the simulation will use in the 
    game.
    """
    def __init__(self, doornum):
        """
        Agrs:
            doornum (int): see class documentation
        
        The __init__() method sets the numdoors attribute equal to the 
        variable "doornum" passed in.
        """
        self.numdoors = doornum
        
    def set_random_doors(self):
        """
        Agrs:
            None (only parameter is self)
            
        This method set_random_doors() will be used to first create a
        list equal to the size of "numdoors". From there, the list is
        filled will the string "zonk" in each position. From there, a
        random position in the list should be replaced by the string "car"
        
        Returns:
            zonk_list (list): A list of length "numdoors" full of strings ("zonk")
        """
        zonk_list = []
        i = 0
        
        while i < self.numdoors:
            zonk_list.append("zonk")
            i+=1
            
        j = 0
        
        while j < 1:
            randpos = random.randrange(0, len(zonk_list))
            zonk_list[randpos] = "car"
            j+=1
        
        return zonk_list
    
    def choose_doors(self):
        """
        Agrs:
            None (only parameter is self)
            
        The method choose_doors() should first call the method 
        set_random_doors() and set it equal to "doors_list". A random item 
        should then be picked and removed from the newly created list, 
        representing a chosen door. After that, one zonk should be removed
        from the list. The final thing this method will do is randomly select
        and remove a door from the list and set it equal to the alternative door.
        
        Returns:
            gamePicks (tuple): contestant's first pick and alternative pick.
        """
        doors_list = Simulation.set_random_doors(self)
        
        k = 0
        
        while k < 1: # "k" < 1 so that while loop only runs once
            randdoor = random.randrange(0, len(doors_list))
            contestant_pick = doors_list[randdoor]
            #doors_list.remove(randdoor)
            
            #The remove command returns an Error. Commented out so code can
            #function properly
            
            k+=1
            
        l = 0
        
        while l < 1: # "l" < 1 so that while loop only runs once
            for x in doors_list:
                if x == "zonk":
                    doors_list.remove(x)
                    
                    randalt = random.randrange(0, len(doors_list))
                    alternative_pick = doors_list[randalt]
                    #doors_list.remove(randalt)
                    
                    #The remove command returns an Error. Commented out so code can
                    #function properly
                    
                    l+=1
        
        gamePicks = contestant_pick, alternative_pick
        
        return gamePicks
            
    def play_game(self, switch = False, iterations = 1):
        """
        Agrs:
            switch (boolean): Contestants decision on door selection
                              (False means they are keeping selection,
                              True means they are switching selection)
            iterations (int): Number of times a person will play the game

        Returns:
            percentage (float): the number of wins the user has gotten out of the 
            numbers of iterations as a decimal
        """
        
        timesWon = 0 #Adds 1 to this whenever if conditions are met
        m = 0 #Adds 1 to this whenever loop finishes a cycle
        
        newGame = Simulation(self.numdoors)
        
        while m < iterations:
            newGameRound = newGame.choose_doors()
            if (newGameRound[0] == "car" and switch == False):
                timesWon+=1
            elif (newGameRound[1] == "car" and switch == True):
                timesWon+=1
            m+=1
        
        percentage = float(timesWon/iterations)
        
        try:
            type(percentage) == float
        except TypeError:
            print("Must be a float value as the output")
        
        return percentage
            
if __name__ == "__main__":
    """
    This method will test run a round of the play_game() function.
    It will create a new instance of Simulation and test a game
    played 1000 times and has the user switch their door each time.
    
    Returns:
        A print out of the win percentages & choose_doors() values
        (for testing purposes)
    """
    mainGame = Simulation(3)
    mainGameRound = mainGame.choose_doors()
    mainGamePlay = mainGame.play_game(True, 1000)
    
    print(mainGamePlay)
    print(mainGameRound)