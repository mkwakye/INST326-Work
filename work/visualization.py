""" A program which visualizes the data from monty_hall.py"""

"""
Driver/Navigator: Michael Kwakye
Email: mkwakye99@gmail.com
Assignment: HW4
Date: 5_11_21
"""

import pandas as pd
import seaborn as sns
import monty_hall


class Plot:
    """
    Agrs:
            doors (int): Number of doors simulation will be based on
            iterations (int): The number of iterations the simulation
                              will be based on
    
    The class Plot has two methods, __init__() and make_plot().
    The __init__() method takes in two parameters doors(int) and
    iterations(int) and uses them to create a list of dictionaries.
    
    Returns:
            make_plot() (Plot object): Returns a visualization of win percentages
            based on iterations and doors
    """
    def __init__(self, doors = 3, iterations = 200):
        """
        Agrs:
            doors (int): see class documentation
            iterations (int): see class documentation
                              
        This method takes in to parameters doors and iterations and uses
        iterations to intialize the length of a loop. If the number of the current 
        iteration is even, the loop will create an instance of Simulation and 
        play_game(), the switch value being set to True. If the number of the current
        iteration is odd, the value of switch will be set to False.
        
        A dictionary holding the values for iterations, percentage, doors and
        switch will be created and appended to the sequence list. After this, a plot
        will be made pretaining using the Plot class.
        
        Returns:
            make_plot() (Plot object): see class documentation
        """
        self.doors = doors
        self.iterations = iterations
        self.sequence = []
        
        # 1 will be added to "m" everytime the loop iterates
        m = 1
        
        while m <= iterations:
            #If statement for even iterations
            if (m%2) == 0:
                montySim = monty_hall.Simulation(doors)
                montyPlayGame = montySim.play_game(True, m)
                
                gameState = {
                    "iterations": m,
                    "percentage": montyPlayGame,
                    "doors": doors,
                    "switched": True
                }
                
                self.sequence.append(gameState)
            
            #If statement for odd iterations
            elif (m%2) == 1:
                montySim = monty_hall.Simulation(doors)
                montyPlayGame = montySim.play_game(False, m)
                
                gameState = {
                    "iterations": m,
                    "percentage": montyPlayGame,
                    "doors": doors,
                    "switched": False
                }
                
            self.sequence.append(gameState)
            m+=1
        
        #Calls make_plot() method
        Plot.make_plot(self)
                
    def make_plot(self):
        """
        Agrs:
            None (only parameter is self)
            
        This method make_plot() creates a dataframe using the pandas module and
        uses it as data for a plot (made with the seaborn module). The result is
        is images that display the data. The number of images is based on the number
        of iterations.
        
        Returns:
            A .PNG of the data visualization
        """
        
        #Creates dataframe using pandas module
        dataframe = pd.DataFrame(self.sequence)
        
        #Creates lmplot using seaborn module
        montyPlot = sns.lmplot(x = "iterations", y = "percentage", data = dataframe, hue = "switched")
        
        #Creates an image which will display the data. 
        #Image name includes the number of iterations and doors
        montyPlot.savefig("montyPlot_" + str(self.iterations) + "_" + str(self.doors))
    
if __name__ == "__main__":
    """
    This method will test plot creation using the Plot class.
    It will create a new instance of Simulation and test to see
    whether make_plot() is functioning correctly.
    """
    Plot(5,100)

        
    
                