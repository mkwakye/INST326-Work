import re
class address:
    def __init__(self,address,city,state):
        self.address = address
        self.city = city
        self.state = state
        
class employee:
    def __init__(self,string):
        self.first_name,self.last_name = parse_name(string)
        add,city,state = parse_address(string)
        self.address = address(add,city,state)
        self.email = parse_email(string)
        
    def parse_name(string):
        string = string.split(" ")#function of re
        string = [string[0],string[1]]
        return tuple(string)
        
    def parse_address(string):
        string = string.split(" ")#function of re
        address = string[2:-3]
        address = " ".join(address)
        city = string[-3]
        state = string[-2]
        return tuple([address,city,state])
        
    def parse_email(string):
        string = string.split(" ")#function of re
        return string[-1]
        
    def main(file_name):
        employee_list = []
        with open(file_name,"r") as file:
            for line in file:
                emp = employee(line)
                employee_list.append(emp)
        
        file.close()
        
        print("Length og employee_list",len(employee_list))
        print("\n\nEMPLOYEE LIST ->")
        
        for i in employee_list:
            print("\n\tFIRST NAME ->\t",i.first_name)
            print("\tLAST NAME ->\t",i.last_name)
            print("\tADDRESS ->\t",i.address.address)
            print("\tCITY ->\t\t",i.address.city)
            print("\tSTATE ->\t",i.address.state)
            print("\tEMAIL ->\t",i.email)

if __name__ == "__main__":
    main("people.txt")