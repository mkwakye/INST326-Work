"""
Driver/Navigator: Michael Kwakye, Nicholas Rudiger
Emails: mkwakye99@gmail.com, nicrudiger@gmail.com
Assignment: Exercise 5
Due Date: 3_10_21

"""
"""Create and manage bookshelf data."""

class Appointment:
    """
    Class Appointment uses the functions __init__(), 
    which creates the attributes "name", start" and "end", and overlaps(),
    which checks if an appointment overlaps with anothers. 
    These will be used to track appointment infromation.
    """
    def __init__(self, name, start, end):
        """
        The function __init__ creates new attributes and 
        has them store information that is passed in. Name should 
        return a string, and "start" and "end" are tuples that
        represent the start and ending times of appointment objects.
        """
        self.name = name
        self.start = ()
        self.end = ()
        
    def overlaps(self, other):
        """
        This function creates a new Appointment object and compares the
        interval for appointment time (using a tuple) and determines 
        whether or not the two appointments overlap
        """ 
        return self.start <= other.start < self.end or self.start < other.end <= self.end
    
        """
        
        OLDER CODE:
        
        if (self.start <= other.start and other.start < self.end):
            return True
        elif (self.start < other.start and other.start >= self.end):
            return False
        elif (other.start <= self.start and self.start < other.end):
            return True
        elif (other.start < self.start and self.start >= other.end):
            return False
        else:
            return True"""