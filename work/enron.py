import re
import argparse
import sys

#\s*(\w*[\s.)]+)[End]* for body
"""
Driver/Navigator: Michael Kwakye
Email: mkwakye99@gmail.com
Assignment: HW3
Date: 4_25_21
"""

class Server:
  """
  This is the Server class, which stores the data 
  for all the emails within a path (text file). 
  This class contains one method (__init__)
  """
  def __init__(self, path):
        """
        This method defines the attributes path and emails, 
        which will be a list composed of Email objects.
        
        The file is first opened and stored into an empty
        string, before being split ad turned into a list of 
        separate emails. From there we iterate through the split
        list of emails and use regex expressions to store components
        of an email into seperate variables. 
        
        These variables are placed into Email objects that are appended
        to self.emails.
        """
        self.path = path
        self.emails = []
        
        
        mail_list = ""
        with open(path) as file:
          for line in file:
            mail_list+=line
        
        split = mail_list.split('End Email"')
        
        
        for x in split:
          message_id = str(re.findall(r"[<]+(\d+\.\d+\.[JavaMail.evans@thyme]+)", x))
          date = str(re.findall(r"(\w+\,+\s\d+\s\w+\s\d+\s\d+\:\d+\:\d+\s\-\d+\s[(PDT)]+)", x))
          subject = str(re.findall(r"\n[Subject:]+\s(.*)", x))
          sender = str(re.findall(r"[From]+\w\:\s(\w+\.+\w+\@\w+\.\w+)", x))
          receiver = str(re.findall(r"\n[To:]+\w\:\s(\w+\.+\w+\@\w+\.\w+)", x))
          body = str(re.findall(r"[X]-FileName:\s[a-z\s(\w-]*[).\w]*\n*([\w\s,?':.()!]*)\n", x))
          
          email = Email(message_id, date, subject, sender, receiver, body)
          self.emails.append(email)
          
        
class Email:
  """
  This is the Email class, which stores the data 
  for indvidual componenents of an email. 
  This class contains one method (__init__)
  """
  def __init__(self, message_id, date, subject, sender, receiver, body):
        """
        This method (__init__) sets the 
        parameters to the corresponding attributes
        """
        self.message_id = message_id
        self.date = date
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.body = body
        
        
def main(path):
  """
  This method creates an instance of the Server class,
  using the path that is passed into the function.
  
  This method returns an integer that represents
  the length of the emails attribute within that instance.
  """
  newServ = Server(path)
  newServLen = len(newServ.emails)
  
  return newServLen
  
def parse_args(args_list):
    """
    This method takes a list of strings from the command prompt and passes them through as
    arguments
    
    args_list is the list of strings from the command prompt
    
    This method returns args (an ArgumentParser object)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type = str)
  
    args = parser.parse_args(args_list)
  
    return args

if __name__ == "__main__":
  """
  This method passes sys.argv[1:] to parse_args() 
  and stores the result in a variable.
  
  This method also calls the main function, using values 
  extracted from the command line.
  """
  #pass
  arguments = parse_args(sys.argv[1:])
  
  main(arguments.required)
             
