#Main module for the game

import random
import time
import sys
from Game import Wordle
from Simplebot import Bot


file = open('sgb-words.txt', 'r')
Ordbok = file.read().splitlines() #Kan testa om ordet finns här innan det gissas, mer effektivt än att ladda varje instans i Game

#Function to check if a word is valid, used for when an user plays
def valid_word(word, nbrofletters):
    return word in Ordbok and len(word) == nbrofletters

#Function for interactive playing
def user_plays(newgame, nbrofletters):
    user_guess = input("Guess the word: ").lower()
    while not valid_word(user_guess,nbrofletters):
        print("Only use valid words and words of length {}".format(nbrofletters))
        user_guess = input("Guess the word: ")


    while newgame.play_round(user_guess):
        print("\n")
        user_guess = input("Guess the word: ")
        while not valid_word(user_guess,nbrofletters):
            print("Only use valid words and words of length {}".format(nbrofletters))
            user_guess = input("Guess the word: ").lower()


#Function for simplebot
def simplebot_plays(newgame, nbrofletters):
    newbot = Bot(ordbok = Ordbok)
    user_guess = newbot.guess()
    print("Current guess: "+user_guess)

    while newgame.play_round(user_guess):
        newbot.read_information(newgame.send_information())
        user_guess = newbot.guess()
        time.sleep(4)
        print("Current guess: "+user_guess)

#Function for AI-bot
def AI_plays(newgame, nbrofletters):
    print("doesnt work yet")


def main():
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = random.choice(Ordbok)
    print("Word to be guessed is: "+word)
    nbrofletters = 5
    Visualize = True

    newgame = Wordle(word, Visualize = Visualize, letters = nbrofletters)

    playstyle = 2

    if playstyle == 1:
        user_plays(newgame, nbrofletters)
    elif playstyle == 2:
        simplebot_plays(newgame, nbrofletters)
    else:
        AI_plays(newgame, nbrofletters)

    return 0

if __name__ == '__main__':
    sys.exit(main())


