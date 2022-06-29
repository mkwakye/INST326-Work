import random

"""
Driver/Navigator: Michael Kwakye
Emails: mkwakye99@gmail.com
Assignment: Exercise 6
Date: 3_23_21

"""

class Player:
    """
    Class Player, which contains the methods __init__().
    This functions creates the name and position attributes, each having a 
    default value.
    """
    def __init__(self, name):
        self.name = name
        self.position = 0
        
class RedPlayer(Player):
    """
    The RedPlayer class is a subclass of the class Player. It contains
    the walk() method.
    """
    def walk(self):
        """
        The walk() method randomly adds a number within the range of
        1 to 10 to the position attribute whenever it is called
        """
        self.position += random.randrange(1,10)
         
class BluePlayer(Player):
    """
    The BluePlayer class is a subclass of the class Player. It contains
    the walk() method, similiar to the class RedPlayer.
    """
    def walk(self):
        """
        The walk() method randomly adds a number within the range of
        4 to 8 to the position attribute whenever it is called
        """
        self.position += random.randrange(4,8)
        
def play_game():
    """
    The method play_game() first creates three instances of both
    RedPlayer and BluePlayer and then stores them into a list.
    
    This list is then iterated over to check and see which player has 
    reached 100 in the position attribute. For each time the loop is
    repeated, the walk() method is called for each respective object in
    the list "player_list".
    
    When a player reaches 100, their name & number of turns (represented
    by "j") are returned.
    """
    player_list = []
    i = 0
    
    while (i < 3):
            redplay = RedPlayer("RedPlayer" + str(i+1))
            blueplay = BluePlayer("BluePlayer" + str(i+1))
            player_list.append(redplay)
            player_list.append(blueplay)
            i+=1
    
    j = 0
    
    while True:
        for x in player_list:
            if(x.position >= 100):
                j+=1
                return (x.name, j)
            else:
                j+=1
                x.walk()
                
        
        
if __name__ == "__main__":
    """
    This method takes the elements within the list returned in "play_game()"
    and prints them separately, denoting both the winner and the number of 
    turns it took them to reach 100 in the position attribute.
    """
    mainplay = play_game()
    print(f"Player {mainplay[0]} has won in {mainplay[1]} turns")