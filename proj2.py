#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Project 2 (User enter 5 sale items, 
#   add them together and apply 6% tax)
#   Date: 4/22/2019

# Initialized variables
subTotal = 0
i = 0

# While loop to run 5 times asking for user input
while i < 5:
    # assigning user input to price
    price = float(input("Enter price of item {num} (excl tax): $".format(num=i+1)))
    # adding user input to subtotal
    subTotal = subTotal + price
    # increment i by 1 until it gets to 5
    i += 1

# Upon exiting while loop, price will apply a 6% tax to the subtotal.
price = float(subTotal * 1.06)

# Prints total with tax with 2 decimal places
print("\nTotal cost (incl 6% tax): ", format(price, '.2f'))