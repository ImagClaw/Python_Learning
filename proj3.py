#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Project 3 (User enter miles driven and gallons used
#   calculates MPG based on input)
#   Date: 4/22/2019

print("Calculates average MPG.")    # Tells user about program
miles = input("Miles traveled: ")   # input miles traveled
gallons = input("Gallons used: ")   # input gallons used

# prints MPG based on input with 2 decimal places
print("You are averaging {mpg:.2f} MPG".format(mpg=(float(miles)/float(gallons))))