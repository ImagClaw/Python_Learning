#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Read from file and reverse
#   Date: 4/24/2019

class Employee:
    def __init__(self, name, idNum, department, jobTitle):
        self.__name = name
        self.__idNum = int(idNum)
        self.__department = department
        self.__jobTitle = jobTitle
    
    def set_name(self, name):
        self.__name = name

    def set_idNum(self, idNum):
        self.__idNum = idNum

    def set_department(self, department):
        self.__department = department

    def set_jobTitle(self, jobTitle):
        self.__jobTitle = jobTitle

    def get_name(self):
        return self.__name

    def get_idNum(self):
        return self.__idNum

    def get_department(self):
        return self.__department

    def get_jobTitle(self):
        return self.__jobTitle



def main():
    input1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    input2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    input3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")


    print(input1.__dict__)
    print(input2.__dict__)
    print(input3.__dict__)



if __name__ == "__main__":
    main()