#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: PersonalInfo class identifies name, address, age, and phone number 
#   We then instantiate the PersonalInfo class with some data, then print it.
#   Date: 4/25/2019

class PersonalInfo:
    def __init__(self, name, address, age, phoneNum):
        self.__name = name
        self.__addres = address
        self.__age = age
        self.__phoneNum = phoneNum

    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__addres = address
    
    def set_age(self, age):
        self.__age = age

    def set_phoneNum(self, phoneNum):
        self.__phoneNum = int(phoneNum)

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__addres

    def get_age(self):
        return self.__age

    def get_phoneNum(self):
        return self.__phoneNum

def main():

    myself = PersonalInfo("Dal", "123 Rd", "32", '210-321-1234')
    mysis = PersonalInfo("Jessica", "124 Blvd", "31", '660-321-1234')
    mymom = PersonalInfo("Janice", "321 Cir", "50", '909-321-1234')
    
    print("I live at: ", myself.get_address())
    print("My mom's name is: ", mymom.get_name())
    print("My sister's phone# is: {phone}".format(phone=mysis.get_phoneNum()))


if __name__ == "__main__":
    main()