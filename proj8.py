#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Project 7 (BMI Calculator) User input weight in lbs 
#   and height in inches to get BMI
#   Date: 4/22/2019


weight = input("Weight in pounds (lbs): ")   # input weight as lbs
kg = float(weight)/2.2046   # converts lbs to kilograms

height = input("Height in inches (in): ")   # input height in inches
m = ((float(height)*0.0254) **2)    # converts inches to meters

# prints approximate BMI with 2 decimal format.
print("Approximate BMI: {bmi:.2f}".format(bmi=float(kg)/float(m))) 