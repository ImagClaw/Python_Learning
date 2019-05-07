#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: For_Range (ranges over 1-4 and multiplies each by 2)
#   Date: 4/23/2019

def main():
    for i in range(4):
        print("2 times {i} = {mul}".format(i=i+1, mul=2*(i+1)))


main()