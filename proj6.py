#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Project 6 (convert minutes into years and days)
#   Date: 4/22/2019

print("Converts minutes into years and days.")
minutes = input("Enter minutes:")

year = int(minutes)/525600  # converts input minutes into years as a solid number
remainingMin = int(minutes) % 525600    # grabs remaining minutes (modulus)
days = remainingMin / 1440  # the modulus of the above is then divied by amount of min in a day

print("\n{min} minutes = {years:.0f} years and {days:.0f} days".format(min=minutes, years=year, days=days))