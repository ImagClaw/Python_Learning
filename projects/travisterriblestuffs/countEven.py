#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project:    Create a count_even_digits() func that takes in 2 params, 
#               the number and the length of the number
#   Date: 5/10/2019

def count_even_digits(digits, length):
    evens = 0
    odds = 0

    print("\n\nHello there useless length input... :wave: @ all {} digits as they are parsed.\n\n".format(length))

    for digit in digits:
        if int(digit) % 2 == 0:
            evens += 1
        else:
            odds += 1

    
        
    return evens, odds

def main():
    usrInput = input("Enter a digit of any length to count how many evens: ")

    evens = count_even_digits(usrInput, len(usrInput))

    print("\n\nThere are {} evens and {} odds in {}\n".format(evens[0], evens[1], usrInput))

if __name__ == "__main__":
    main()