#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project:    Write a while loop that lets the user enter a number. 
#               The number should be multipliedby 10, and the result assigned to a 
#               variable named product. The loop should iterate aslong as product is 
#               less than 100.
#   Date:5/7/2019


def main():
    product = 0
    num = float(input("Enter a number to be multiplied by 10: "))

    while product < 100:
        print("Your number multiplied by 10 (until reaching 100): {:.2f}".format(product))
        product += (num * 10)
        

if __name__ == "__main__":
    main()