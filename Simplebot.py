#Plays the game with the very simple strat of eliminating words, hoping to narrowing it down to 1
import random

class Bot:
    def __init__(self, ordbok):
        self.ordbok = ordbok
        self.known_letters = {}
        self.unknown_letters = {}
    
    #Makes a random guess from the remaining possible words
    def guess(self):
        word = random.choice(self.ordbok)
        return word

    #Takes information it is fed from Game.py, uses update_list to update possible words
    def read_information(self, input_data):
        board = input_data[0]
        colours = input_data[1]
        alphabet = input_data[2]
        curr_row = input_data[3]
        self.update_list(alphabet, curr_row, colours, board)
    

    #Updates possible words
    def update_list(self, alphabet, curr_row, colours, board):
        keep_letters = [k for k,v in alphabet.items() if v == 2]
        keep_list = []
        for i in range(5):
            if colours[curr_row-1][i] == 2:
                self.known_letters[i] = board[curr_row-1][i]
            elif colours[curr_row-1][i] == 1:
                if i in self.unknown_letters:
                    self.unknown_letters[i].append(board[curr_row-1][i])
                else:
                    self.unknown_letters[i] = [board[curr_row-1][i]]
        
        for word in self.ordbok:
            keep = True

            for letter in keep_letters:
                if letter not in word:
                    keep = False
            
            for i in range(5):
                letter = word[i]
                if i in self.known_letters and letter != self.known_letters[i]:
                    keep = False
                elif i in self.unknown_letters and letter in self.unknown_letters[i]:
                    keep = False
                elif alphabet[letter] == 0:
                    keep = False
            
            if keep:
                keep_list.append(word)
        
        self.ordbok = keep_list

            
