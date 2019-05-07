#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Search a list of names, if Ruby exists print 
#   "Hello Ruby.", else print "No Ruby.".
#   Date: 4/24/2019


names = ["Einstein", "Newton", "Copernicus", "Kepler"]

def main():
    if "Ruby" not in names and "ruby" not in names:
        print("No Ruby, ¯\\_(ツ)_/¯")
    else:
        print("Hello Ruby, o/")

if __name__ == "__main__":
    main()