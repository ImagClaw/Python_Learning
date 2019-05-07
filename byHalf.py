#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project:    The following statement calls a function named half, which returns 
#               a value that is halfthat of the argument. (Assume the number 
#               variable references a float value.)Writecode for the function.
#               result = half(number)
#   Date:5/7/2019

def half(num):
    num /= 2
    return num

def main():
    num = int(input("Enter a nunmber to he halfed: "))
    
    print("Your number halfed is {:.2f}".format(half(num)))


if __name__ == "__main__":
    main()