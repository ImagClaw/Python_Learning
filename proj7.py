#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Project 7 (Physics: Acceleration)
#   Date: 4/22/2019

v0 = input("Enter v0 (starting velocity in m/s): ") # input v0
v1 = input("Enter v1 (ending velocity in m/s): ")   # input v1
t = input("Enter the travel time: ")    # input t

# Prints approximate acceleration with 4 decimal format
print("Approximate acceleration: {accel:.4f} m/s".format(accel=(float(v1)-float(v0))/float(t)))