#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: reverse it and check if palindrome
#   Date: 4/23/2019

# reverse, reverses the input number
def reverse(number):
    print("Your {num1} reversed is {num2}".format(num1=number, num2=number[::-1]))
    if isPalindrome(number) == True:
        print("\nOgden is not right and this is also a Palindrome! Win Win!")
    else:
        print("\nIt is, sadly, NOT a Palindrome. But Ogden is still not right. =(")

# isPalindrome checks if the input reverse is the same and is not really needed...
def isPalindrome(turd):
    if turd == turd[::-1]:
        return True
    else:
        return False


def main():
    userIn = input("Enter a number to reverse: ")
    if isinstance(userIn, int) == False:
        reverse(userIn)
    else:
        print("What you entered is NOT an integer. Try again.")

if __name__ == "__main__":
    main()