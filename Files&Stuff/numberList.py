#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project:    Write code that does the following: opens an output 
#               file with the filenamenumber_list.txt, uses a loop to 
#               write the numbers 1 through 100 to the file, and then
#               closes the file.
#   Date:5/7/2019

def main():
    i = 0
    f = open("number_list.txt", "w+")

    while i < 101:
        f.write(str(i)+"\n")
        i += 1

    f.close()


if __name__ == "__main__":
    main()