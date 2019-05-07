#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Pet Class build and then instantiation or the class
#   Date: 4/25/2019

class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


def main():
    
    name = input("What is your pet's name?\n")
    animal_type = input("What type of pet is {name}?\n".format(name=name))
    
    if animal_type == "dog":
        age = input("Heck yeah! Dogs are awesome.  How old is {name}?\n".format(name=name))
    #if else animal_type == "lizard":
    #    age = input("Disgusting! Why??? Fine,ow old is {name}?\n".format(name=name))
    else:
        age = input("How old is {name}?\n".format(name=name))
    
    pets = Pet(name, animal_type, age)

    
    print('Here is the data you entered:')
    print('Pet Name: ', pets.get_name())
    print('Animal Type: ', pets.get_animal_type())
    print('Age: ', pets.get_age())
    print('This will be added to the records. ')

if __name__ == "__main__":
    main()