#Can estimate average number of tries and average win rate using MC simulation

from Game import Wordle
from Simplebot import Bot
import random
import sys
import numpy as np
import matplotlib.pyplot as plt
file = open('sgb-words.txt', 'r')
Ordbok = file.read().splitlines()

#1 is simplebot, 2 is AI
mode = 1

def simplebot(newgame):
    newbot = Bot(ordbok = Ordbok)
    user_guess = newbot.guess()

    while newgame.play_round(user_guess):
        newbot.read_information(newgame.send_information())
        user_guess = newbot.guess()
    
    nbroftries = newgame.send_information()[3]+1
    if nbroftries <= 6:
        return nbroftries
    return 0

def aibot(word):
    return 1

def main():
    N = 1000 #nbrofsimulations

    res = np.zeros(N)
    for i in range(N):
        word = random.choice(Ordbok)
        newgame = Wordle(word, Visualize = False)

        if mode == 1:
            nbroftries = simplebot(newgame)
        elif mode == 2:
            nbroftries = aibot(word)

        res[i] = nbroftries

    res_new = res[res != 0]
    print("Percentage correct: "+str(100*len(res_new)/N))
    print("Average amount of guesses: "+str(np.mean(res_new)))

if __name__ == '__main__':
    sys.exit(main())