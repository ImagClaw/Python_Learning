#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Create a list of names, iterate through that list
#   and print the names.
#   Date: 4/24/2019


names = ["Einstein", "Newton", "Copernicus", "Kepler"]

def main():
    for item in names:
        print(item, end=", ")

if __name__ == "__main__":
    main()