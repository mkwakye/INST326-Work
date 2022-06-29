class University:
    """
    """
    def __init__(self, students_enrolled, conference):
        self.students_enrolled = students_enrolled
        self.conference = conference
        self.departments = [] 
        #prompt said the value is a string but also says it is a list
        #kept it as a list
        
class Departments:
    """
    """
    def __init__(self, employee_count, location):
        self.employee_count = employee_count
        self.location = location
        
class College(Departments):
    """
    """
    
umcp = College(1574, "College Park")
umd = University(28783, "ACC")

add_department = umd.departments.append(umcp)

#CODE TO TEST
print(umd.students_enrolled)
    