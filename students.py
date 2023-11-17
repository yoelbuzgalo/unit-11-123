"""
A Student class.

@author GCCIS Faculty
"""

GRADES = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F", "NG"]

QUALITY_POINTS = {
    GRADES[0]: 4.0,
    GRADES[1]: 3.67,
    GRADES[2]: 3.33,
    GRADES[3]: 3.0,
    GRADES[4]: 2.67,
    GRADES[5]: 2.33,
    GRADES[6]: 2.0,
    GRADES[7]: 1.67,
    GRADES[8]: 1.0,
    GRADES[9]: 0,
    GRADES[10]: 0 # no grade
}

class Student:
    """
    A class that represents a student with fields for ID, name, credits, and
    GPA.
    """
    __slots__ = ["__id", "__name", "__credits", "__gpa"]

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__credits = 0
        self.__gpa = 0

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_credits(self):
        return self.__credits
    
    def get_gpa(self):
        return self.__gpa

    def print(self):
        """
        Prints a student's info to standard output.
        """
        print("Student: ID=", self.__id, ", name=", self.__name, 
            ", credits=", self.__credits, ", GPA=", self.__gpa, sep="")