#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project:    Write a for loop that displays the following set of 
#               numbers:0, 10, 20, 30, 40, 50 . . . 1000
#   Date:5/7/2019

def main():
    num = 0

    while num < 1001:
        print(num)
        num += 10
        

if __name__ == "__main__":
    main()