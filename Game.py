#Writing the Game console for Wordle


class Wordle:
    def __init__(self, word, rows = 6, letters = 5, Visualize = False):
        self.curr_row = 0
        self.word = word
        self.rows = rows
        self.letters = letters
        self.alph = {}
        #0 = letter isnt in word, 1 it might be, 2 means it definitely is
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            self.alph[letter] = 1
        self.Visualize = Visualize
        self.board = [[' ' for i in range(letters)] for j in range(rows)]
        #0 = gray, 1 = yellow, 2 = green
        self.colours = [['' for i in range(letters)] for j in range(rows)]


    #Takes a user input as a guess and adds it to the board
    def guess(self,user_input):
        i = 0
        for letter in user_input:
            self.board[self.curr_row][i] = letter
            if letter == self.word[i]:
                self.colours[self.curr_row][i] = 2
                self.alph[letter] = 2
            elif letter in self.word:
                self.colours[self.curr_row][i] = 1
                self.alph[letter] = 2
            else:
                self.colours[self.curr_row][i] = 0
                self.alph[letter] = 0

            i += 1
        return

    #Return 0 if game is lost, return 1 if game is ongoing, return 2 if game is won
    def update_game(self):
        complete = True
        for i in range(self.letters):
            if self.board[self.curr_row][i] != self.word[i]:
                complete = False
        
        if complete:
            return 2

        self.curr_row += 1
        if self.curr_row >= self.rows:
            return 0

        return

    #Printing the board for visualization
    def show_board(self):
        for i in range(self.rows):
            print(self.board[i])
        print("\n")
        for i in range(self.rows):
            print(self.colours[i])
        #print(self.alph)
        print("\n")

    #Main function, the only one to be used
    #Plays a round, returns 0 if you lose, otherwise returns how many tries it took you
    def play_round(self, user_guess):
        ongoing = True
        self.guess(user_guess)
        if self.Visualize:
            self.show_board()

        state = self.update_game()
        if state == 0:
            if self.Visualize:
                print("Game over, better luck next time")
            ongoing = False
        elif state == 2:
            if self.Visualize:
                print("Congratulations, you won on: {} tries".format(self.curr_row+1))
            ongoing = False
        
        return ongoing

    #Sends information to a bot directly
    def send_information(self):
        return self.board, self.colours, self.alph, self.curr_row