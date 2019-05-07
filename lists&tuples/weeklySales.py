#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Prompt user for daily sales input, add to list, print list total.
#   Date: 4/24/2019

days = ("Sunday", "Monday", 
        "Tuesday", "Wednesday", 
        "Thursday", "Friday", 
        "Saturday")

dailySales = []

def main():
    weeklyTotal = 0
    for i in range(7):
        weeklyTotal = float(weeklyTotal) + float(input("Enter sale total for {day}: $".format(day=days[i])))

    print()
    print("Total sales for the week: ${tot:.2f}".format(tot=float(weeklyTotal)))


if __name__ == "__main__":
    main()