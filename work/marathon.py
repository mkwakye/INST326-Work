import random
import players

"""
Driver/Navigator: Michael Kwakye
Emails: mkwakye99@gmail.com
Assignment: Exercise 6
Date: 3_23_21

"""

def play_game():
    """
    The method play_game() first creates three instances of both
    RedPlayer and BluePlayer (imported from player.py) and then 
    stores them into a list.
    
    This list is then iterated over to check and see which player has 
    reached 1000 in the position attribute. For each time the loop is
    repeated, the walk() method is called for each respective object in
    the list "player_list".
    
    When a player reaches 1000, their name & number of turns (represented
    by "j") are returned.
    """
    player_list = []
    i = 0
    
    while (i < 3):
            redplay = players.RedPlayer("RedPlayer" + str(i+1))
            blueplay = players.BluePlayer("BluePlayer" + str(i+1))
            player_list.append(redplay)
            player_list.append(blueplay)
            i+=1
    
    j = 0
    
    while True:
        for x in player_list:
            if(x.position >= 1000):
                j+=1
                return (x.name, j)
            else:
                j+=1
                x.walk()
                
        
if __name__ == "__main__":
    """
    This method takes the elements within the list returned in "play_game()"
    and prints them separately, denoting the first player to reach 100 in 
    the position attribute and 1000 in the position attribute.
    """
    mainplay = play_game()
    playersplay = players.play_game()
    print(f"Player {mainplay[0]} has won the marathon in {mainplay[1]} turns")
    print(f"Player {playersplay[0]} has won in {playersplay[1]} turns")