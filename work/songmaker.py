"""
Driver/Navigator: Michael Kwakye, Nicholas Rudiger
Emails: mkwakye99@gmail.com, nicrudiger@gmail.com
Assignment: Exercise 4
Due Date: 3_3_21

"""

from argparse import ArgumentParser
import math
import sys

class Song:
    """
    Class Book, which contains the methods __init__() and unique_words().
    These functions intialize the object Book (init) and then manipulates 
    its attributes (unique_words)
    """
    def __init__(self, name, primary_artist, bpm, chords):
        """
        """
        chords = []
        self.name = name
        self.artists = primary_artist
        self.bpm = bpm
        self.chords = chords
        
    
    def associated_artists(self, other_artist):
        """
        This method appends associated artists that are passed in to the
        artist parameter in __init__
        """
        other_artist.append(self.artists)
        
    def change_beat(self, increase = True, change = 5):
        """
        This method increases the bpm if the parameter "increase" is True, 
        as well as decreasing the bpm if "increase" is equal to False. The
        amount the bpm is increased/decreased by is dependent on the 
        parameter "change"
        """
        if (increase == True):
            self.bpm+=change
        elif (increase == False):
            self.bpm-=change
            
    def modulate(self, steps = 1):
        """
        This method determines the correct modulated chord from a list
        based on the positon of a note in a list and a "steps" value passed
        in. This modulated chord is then stored into a empty list. 
        Once all the notes are modulated, the function should set the 
        parameter "chords" equal to the brand new list.
        """
        chord_notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
        chord_modulated = []
        
        i = 0
        while (i < len(chord_notes)):
            if (steps % 1 == 0):
                chord_modulated.append(chord_notes[i+(2*steps)])
            elif (steps % 0.5 == 0):
                chord_modulated.append(chord_notes[i+(2*steps)])
            i+=1
            
            
        self.chords = chord_modulated
    
    def info(self):
        """
        This function prints a message indciating to the user the song's
        name, artists, chords and bpm (beats per minute)
        """
        print("Song: ", self.name, ", Artist(s): ", self.artists, 
              ", Chords: ", self.chords, ", BPM: ", self.bpm)
        
if __name__ == "__main__":
    new_song = Song(name = "Thriller", primary_artist = "Michael Jackson", bpm = 120, chords = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'])
    
    new_song.change_beat(True, 10)
    new_song.modulate(1)
    
    assert new_song.name == "Thriller"
    assert new_song.artists == "Michael Jackson"
    assert new_song.bpm == 130