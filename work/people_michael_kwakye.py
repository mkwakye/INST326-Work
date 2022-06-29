import re

"""
Driver/Navigator: Michael Kwakye
Emails: mkwakye99@gmail.com
Assignment: Exercise 7
Date: 3_31_21

"""

def parse_name(text):
    """
    This function contains one parameter, text, which represents a line
    in a file. This function makes use of the re module/regular
    expressions to take the first and last names of indivudals,
    then returns the pairing as a tuple.
    """
    first_name = str(re.findall(r"(^[A-Za-z]+\w\b)", text))
    last_name = str(re.findall(r"\s([A-Za-z]{3,})\s\d", text))
    first_last = (str(first_name),str(last_name))
    
    return first_last

def parse_address(text):
    """
    This function contains one parameter, text, which represents a line
    in a file. This function also makes use of the re module/regular
    expressions to take the street, city and state from the text, 
    seperating each component and then returning an address object.
    """
    street = str(re.findall(r"(\d.*)\s\w+\s[A-Z]*\s", text))
    city = str(re.findall(r"\s(\w+)\s[A-Z]*\s", text))
    state = str(re.findall(r"\s([A-Za-z]{2})\s", text))
    
    add = address(street, city, state)
    
    return add

def parse_email(text):
    """
    This function contains one parameter, text, which represents a line
    in a file. This method uses re module/regular expressions to take 
    the email address for each individual from the file and returns
    this value as a string.
    """
    email = str(re.findall(r"[A-Z]\s(\w.*[@]\w*[.]\w+)", text))
    
    return email

class address:
    """
    The class address has three attributes: street, city and state. This 
    function has no methods, simply creating the attributes which will be
    the arguments for the instance of address when it is called.
    """
    def __init__(self,street,city,state):
        """
        Creates the attributes street, city and state.
        """
        self.street = street
        self.city = city
        self.state = state
    
class employee:
    """
    The class employee has four attributes: first_name, last_name, city,
    and state. Using the three methods created before (parse_name, 
    parse_address, parse_email), the attributes are set equal to their 
    respective methods. For example, the first_name and last_name 
    attributes are taken from the tuple created when parse_name is called.
    """
    def __init__(self,text):
        """
        Creates the four attributes of employee.
        """
        name = parse_name(text)
        self.first_name = name[0]
        self.last_name = name[1]
        self.address = parse_address(text)
        self.email = parse_email(text)
        
def main():
    """
    This function main() creates a empty employee_list that will be 
    populated by passing in the lines read from the employee object called.
    Each line in the file opened will be stored into the employee object,
    which is then stored into the employee_list.
    
    After this is completed, the function will print out each component
    of the object (first and last name, address, etc). The length of the 
    list will also be printed, representing the number of employees.
    """
    employee_list = []
    with open("people.txt") as file:
        for line in file:
            emp = employee(line)
            employee_list.append(emp)
    file.close()
    
    count = 1
    for i in employee_list:
        print("Employee #" + str(count))
        
        print("First Name: " + i.first_name)
        print("Last Name: " + i.last_name)
        print("Street: " + i.address.street)
        print("City: " + i.address.city)
        print("State (Abbreviation): " + i.address.state)
        print("Email Address: " + i.email + "\n")
        count+=1
        
    print("The number of employees is " + str(len(employee_list)) + "\n")
    
if __name__ == "__main__":
    """
    Calls the main function using the "people.txt" file as the source.
    """
    main()