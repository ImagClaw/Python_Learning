#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Car Class build and then instantiation or the class
#   Date: 4/25/2019

class Car:
    def __init__(self, year, model, make, speed):
        self.__year = year
        self.__model = model
        self.__make = make
        self.__speed = 0

    def set_year(self, year):
        self.__year = year

    def set_model(self, model):
        self.__model = model
    
    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = 0

    def get_year(self):
        return self.__year

    def get_model(self):
        return self.__model

    def get_make(self):
        return self.__make


    # METHODS
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

def main():
    make = input("What make is your vehicle? ")
    model = input("What model of {make}? ".format(make=make))
    year = input("What year is your {make} {model}? ".format(make=make, model=model))
    speed = 0

    car = Car(year, model, make, speed)

    # Accelerate 5 times
    print('The current speed is: ', car.get_speed())
    car.accelerate()
    print('The current speed is: ', car.get_speed())
    car.accelerate()
    print('The current speed is: ', car.get_speed())
    car.accelerate()
    print('The current speed is: ', car.get_speed())
    car.accelerate()
    print('The current speed is: ', car.get_speed())
    car.accelerate()
    print('The current speed is: ', car.get_speed()) 

    print("\n\n\n\nTime to slow down... \n\n\n")

    # Brake 5 times
    print('The current speed is: ', car.get_speed())
    car.brake()
    print('The current speed is: ', car.get_speed())
    car.brake()
    print('The current speed is: ', car.get_speed())
    car.brake()
    print('The current speed is: ', car.get_speed())
    car.brake()
    print('The current speed is: ', car.get_speed())
    car.brake()
    print('The current speed is: ', car.get_speed())

if __name__ == "__main__":
    main()