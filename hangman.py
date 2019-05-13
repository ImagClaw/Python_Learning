#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project:    Write a hangman game that randomly generates a word and
#               prompts the user to guess one letter at a time, as shown 
#               in the sample run. Each letter in the word is displayed 
#               as an asterisk. When the user makes a correct guess, the 
#               actual letter is then displayed. When the user finishes a 
#               word, display the number of misses and ask the user whether 
#               to continue playing. Createa list to store the words, as follows
#   Date:5/13/2019

import random

WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")


def main():
    word = random.choice(WORDS)
    ast = "*" * len(word)
    playagain = True
    wrongGuess = 0
    
    while ast != word and playagain == True:
        guess = input("Enter your a letter in word {} > ".format(ast))
        if guess == word:
            print("Fuck yeah, the word is '{}', nice job!".format(str(word)))
            again = input("Would you like to play again? (yes or no): ")
            if again == 'no':
                return playagain == False
            elif again == 'yes':
                main()
        elif len(guess) != 1:
            print("You must guess exactly 1 letter or your guess is wrong try again.")
        elif guess in word:
            if guess in ast:
                print("{} is already in the word.".format(guess))
            else:
                ast = update_asterisk(word, ast, guess)
        else:
            print("Letter not in the word.")
            wrongGuess +=1
    
    print("The word is '{}' and you guessed {} wrong letters.".format(word, wrongGuess))


def update_asterisk(word, curr_asterisk, curr_guess):
    result = ""
    for i in range(len(word)):
      if word[i] == curr_guess:
        result = result + curr_guess     # Adds guess to string if guess is correctly
      else:
        # Add the dash at index i to result if it doesn't match the guess
        result = result + curr_asterisk[i]

    return result


if __name__ == "__main__":
    main()