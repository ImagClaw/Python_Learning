#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Create a 2-Dimensional array with 5 rows and 3 columns, write
#   a nested loop to get an integer value from user to fill each element.
#   Date: 4/24/2019

import random



def main():
    arrayFin = []  # Empty array to be filled

    # Prompt user for input to random func
    userIn = int(input("Enter a number to be the max of a random range (ie, 100): "))

    # for i in range(5) creates the rows
    for _ in range(5):
        column = []
        # for j in range(3) fills column with random number
        for _ in range(3):
            rando = random.randrange(userIn+1)    # Generates a random num for input (user supplied randrange max)
            column.append(rando)    # appends random number to column list
        arrayFin.append(column)    # appends column list to arrayFin

    print(arrayFin)

if __name__ == "__main__":
    main()