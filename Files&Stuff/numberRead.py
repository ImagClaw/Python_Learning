#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project:    Write code that does the following: opens the 
#               number_list.txt file that was createdby the code 
#               you wrote in the previous question , reads all of 
#               the numbers from the file and displays them, and then 
#               closes the file.
#   Date:5/7/2019

def main():

    with open("number_list.txt") as f:
        print(", ".join(line.strip() for line in f))

if __name__ == "__main__":
    main()