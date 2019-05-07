#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Rainfall over 12 months, display total rainfall, 
#   average monthly rainfall, highest and lowest rainfall months
#   Date: 4/24/2019

months = ("January", 
            "February", 
            "March", 
            "April", 
            "May", 
            "June", 
            "July",
            "August", 
            "September", 
            "October", 
            "November", 
            "December")

rainfallPerMon = []

def main():
    mon = 0
    total = 0

    while mon < 12:
        rainfall = input("Enter the rainfall for {mon} (in inches): ".format(mon=months[mon]))
        rainfallPerMon.append(int(rainfall))
        mon +=1
    for item in rainfallPerMon:
        total = float(total) + float(item)

    print()
    print("The total rainfall is {total:.2f} inches.".format(total=float(total)))
    print()
    print("The average rainfall per month is {avg:.2f} inches.".format(avg=float(total)/12))
    print()
    print("The month with the lowest rainfall is {mon} with {rain:.2f} inches.".format(mon=months[int(rainfallPerMon.index(min(rainfallPerMon)))], 
                                                    rain=float(min(rainfallPerMon))))
    print()
    print("The month with the highest rainfall is {mon} with {rain:.2f} inches.".format(mon=months[int(rainfallPerMon.index(max(rainfallPerMon)))], 
                                                    rain=float(max(rainfallPerMon))))


if __name__ == "__main__":
    main()