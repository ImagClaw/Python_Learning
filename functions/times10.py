#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: times10 () 
#   and height in inches to get BMI
#   Date: 4/22/2019

def times_ten(x=0):
    return float(x) * 10

def show_value(quantity):
    return quantity

inputNum = input("Enter a number: ")
print("{inputnum:.0f} x 10 = {num:.2f}".format(inputnum=float(inputNum), num=float(times_ten(show_value(inputNum)))))