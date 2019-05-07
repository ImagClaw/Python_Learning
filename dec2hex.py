#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Deimal to Hexidecimal CLI
#   Date: 4/23/2019

decIn = int(input("Enter a decimal number to convert to hex: "))
print("{dec} converted to hex is: {hexd}".format(dec=decIn, hexd=hex(decIn)))