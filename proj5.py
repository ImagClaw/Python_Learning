#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Project 5 (convert feet to meters)
#   Date: 4/22/2019

print("Convert feet to meters.")    # tells user about program
feet = input("Enter feet:") # input feet

# converts feet to meters with 2 decimal places format
print("{feet:.2f} ft = {meters:.3f} m".format(feet=float(feet), meters=float(feet)/3.28))