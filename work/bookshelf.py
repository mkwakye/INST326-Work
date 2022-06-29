"""Create and manage bookshelf data."""
from argparse import ArgumentParser
import math
import sys



def remove_punctuation(word):
    """
    Takes in a string passed in from the user and returns a lowercase
    version of that word. If the string contains no characters,
    the function will instead return None.
    """
    new_word = " "
    letter_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ"

    try:
        type(word) == str
    except TypeError:
        print("Only strings can be passed into this function")
    
    """if word:
        for x in word:
            if (x.isalpha() == True):
                new_word+=x
    else:
        return None"""
    if word:
        for x in word:
            if x in letter_list or x.isalpha() == True:
                new_word += x
            else:
                return None
                
    elif word == "":
        return None
        
    return new_word.lower()

class Book:
    """
    Class Book, which contains the methods __init__() and unique_words().
    These functions intialize the object Book (init) and then manipulates 
    its attributes (unique_words)
    """
    def __init__(self, path):
        """
        This method creates a list for the words attribute and
        stores the content of the path parameter into it. After 
        calling the remove_punctuaation method and storing the new
        values in an empty list, the contents of punc_list are
        looped into the words attribute.
        """
        
        new_path= open(path, "r")
        words_path = new_path.read()
        
        self.words = [remove_punctuation(x) for x in words_path]
        
        """for x in self.words:
            if remove_punctuation(x) == None:
                self.words.remove(x)"""
        
        
    
    def unique_words(self):
        """
        This method creates a set based on the words attribute
        """
        unique_set = set()
        
        for x in self.words:
            unique_set.add(x)
            
        return unique_set

class Bookshelf:
    """
    Class Bookshelf, which contains the methods __init__(), add_books() 
    and find_popularity.
    """
    def __init__(self):
        """
        This method creates the attributes index and popularity_index
        """
        self.index = {}
        self.popularity_index = {}
        
    def add_books(self, text):
        """
        This method creates a new book instance and using the 
        unique_words method, adds the contents of text into the index
        attribute.
        
        """
        next_book = Book(text)
        next_book_unqiue = next_book.unique_words()
        
        for x, y in next_book_unqiue:
            self.index[x].append(y)
        
    def find_popularity(self):
        """
        This method resets the popularity_index and populates it
        by iterating over items within the index attribute.
        """
        self.popularity_index = {}
        for key, value in self.index.items():
            self.index[key].append(value)
    
def main(library):
    """
    This method creates an instance of bookshelf using the library parameter
    passed in. The list (library) will be used to invoke add_books and
    find_popularity
    """
    new_shelf = Bookshelf()
    new_pop = {}

    for x in library:
        new_shelf.add_books(x)
        new_pop = new_shelf.find_popularity(x)
    
    return new_shelf, len(new_shelf), new_pop

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
    arguments
    Args:
    args_list (list) : the list of strings from the command prompt
    Returns:
    args (ArgumentParser)
    """
    parser = ArgumentParser()
    parser.add_argument('books', type = str, help = 'This represents a book object', nargs="+")
  
    args = parser.parse_args(args_list)
  
    return args
    
if __name__ == "__main__":
  try:
    args = parse_args(sys.argv[1:])
  except ValueError as e:
    sys.exit(str(e))
    
    """library = open("C:/Users/tmwar/OneDrive/Documents/2021 SEMESTER/INST326/work/data")
    main(library)"""
  main(args.books)
  print(main(args.books))
