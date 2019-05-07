#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Exchange Rate read file.
#   Date: 5/3/2019
import time

def main():
    
    t = time.ctime()
    print(t)
    f = open("Exchrate.txt", "r")

    country = input('Enter the name of a country: ')
    country = country.lower()  

    for line in f:  
        line = line.strip() 
        data = line.split(',') 

        if data[0].lower() == country:
            print("\n Currency: {} \n Exchange Rate: {:.2f}".format(data[1], float(data[2])))
            break
            


if __name__ == "__main__":
    main()