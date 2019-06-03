import os
from test_module import ERROR_NOT_FOUND, ERROR_INVALID

# STUDENT SECTION

#Given a directory, traverse through all sub-directories and build a dictionary with the directory as the key and a list
#of the .txt files as the value
def FileDict(dir):
    fileDict = {}
    for (rootpath, _, filename) in os.walk(dir):
        for files in filename:
            print(rootpath)
            if files.endswith(".txt"):
                print(files)

    return fileDict

#Given a string, find all occurrences of badLtr and replace them with goodLtr. If you cannot find any
#of badLtr, return ERROR_NOT_FOUND. If an invalid string is passed in, return ERROR_INVALID
def ChangeLetter(inputStr, badLtr, goodLtr):
    if not inputStr:
        return ERROR_INVALID

    if badLtr in inputStr:
        outputStr = inputStr.replace(badLtr, goodLtr)
        return outputStr
    else:
        return ERROR_NOT_FOUND
    

#Given a string and a word, find the word in the sentence and reverse it. Return the corrected string if the word is
#found, or ERROR_NOT_FOUND if the word is not in the string, or ERROR_INVALID if a parameter is invalid
def ReverseWord(inputStr, revWord):
    if not inputStr:
        return ERROR_INVALID
    if revWord in inputStr:
        return inputStr.replace(revWord, revWord[::-1])
    else:
        return ERROR_NOT_FOUND

#Given a string and a key, XOR each letter with the key and return the string. If a parameter is invalid, return
#ERROR_INVALID
def ObfuscateString(inputStr, key):
    if not inputStr or not key:
        return ERROR_INVALID

    stuffs = []

    for char in inputStr:
        stuffs.append(chr(ord(char)^key))

    return ''.join(stuffs)


#Given two strings, combine them and return the total string. If a parameter is invalid, return ERROR_INVALID
def CombineStrings(string1, string2):
    if not string1 or not string2:
        return ERROR_INVALID
    else:
        outputStr = string1 + string2
        return outputStr

#Given a string, insert the given word behind the target word. For instance, if given the sentence "insert the here",
#with the word to be inserted as "word" and the target as "the", the final string should be "insert the word here".
#If any parameter is invalid, return ERROR_INVALID
def InsertWord(inputStr, word, target):
    if not inputStr or not word:
        return ERROR_INVALID

    if target in inputStr:
        return inputStr.replace(target, target + word)
    else: 
        return ERROR_NOT_FOUND

#Given a string and a word, delete the word from the string and return the modified string. If the target word cannot
#be found, return ERROR_NOT_FOUND.
def DeleteWord(inputStr, word):
    if not inputStr:
        return ERROR_INVALID
    
    if word in inputStr:
        return inputStr.replace(word, '')
    else: 
        return ERROR_NOT_FOUND