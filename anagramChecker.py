#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project:    Write a function that checks whether two words are 
#               anagrams.Two words are anagrams if they contain the 
#               same letters. For example, silent and listen are 
#               anagrams. The header of the function is:
#               def isAnagram(s1, s2):
#   Date:5/13/2019

def isAnagram(s1, s2):  
    # Get lengths of both strings  
    n1 = len(s1)  
    n2 = len(s2)  

    # Compare length, if not same, not an anagram  
    if n1 != n2:  
        return 0
  
    # Sort strings in alphabetical order  
    s1 = sorted(s1) 
    s2 = sorted(s2) 
  
    # Compare sorted strings, if sorted strings do not match, not an anagram  
    for i in range(0, n1):  
        if s1[i] != s2[i]:  
            return 0
    return 1
  
  
def main():
    input1 = input("Enter the the first word: ")
    input2 = input("Enter the the second word: ")

    if isAnagram(input1, input2):  
        print ("The two strings are anagram of each other") 
    else:  
        print ("The two strings are not anagram of each other")

if __name__ == "__main__":
    main()