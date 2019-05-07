#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Project 1 (User enter sale, 
#   shows 23% profit)
#   Date: 4/22/2019


sale = float(input("Enter sale price: $"))  #prompt user for sale input
profit = float(sale * 0.23) # calculates 23% of user input

# Prints wholesale cost was of the product sold
print("\nWholesale cost: $", format((sale - profit), '.2f'))
# Prints user profit
print("Profit from sale: $", format(profit, '.2f'))