#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Prompt user for 20 integers as input, add to list, find the highest,
#   lowest, average, and total for all numbers input.
#   Date: 4/24/2019

userInput = []

def main():
    total = 0
    for i in range(20):
        userInput.append(input("Enter #{num} integer:".format(num=i+1)))

    for item in userInput:
        total = total + int(item)
    
    print()
    print("The lowest number you input is: {low}.".format(low=int(min(userInput))))
    print()
    print("The highset number you input is: {high}".format(high=int(max(userInput))))
    print()
    print("The average of all numbers you input is: {avg:.2f}".format(avg=float(total)/20))
    print()
    print("The total of all numbers is: ", total)

if __name__ == "__main__":
    main()