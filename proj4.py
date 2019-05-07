#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Project 4 (convert Celsius to Fehrenheit)
#   Date: 4/22/2019

print("Converts Celsius to Fehrenheit.")    # Tells user about program
c = input("Enter the temp in Celsius: ")    # input tempurature in celsius

f = float(9/5)*float(c)+32  # converts input to fehrenheit

# prints Celsius input and Fehrenheit conversion with 1 decimal place
print("\n{cels:.1f} °C = {fehr:.1f} °F".format(cels=float(c), fehr=float(f)))