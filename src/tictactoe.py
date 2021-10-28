import os


class TicTacToe:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.player = 1
        self.gametype = 0

    def menu(self):
        string = "Welcome to TicTacToe\n" +\
                 "Choose one of the following options:\n" +\
                 "v: To play versus another player\n" + \
                 "q: to quit\n"

        self.page_clear()
        print(string)
        user_choice = input(">")
        if user_choice == "q":
            return
        elif user_choice == "v":
            self.game_player()

    def _board_string(self):
        string = ""
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == 0:
                    string += " "
                elif self.board[x][y] == 1:
                    string += "X"
                else:
                    string += "O"
                if y < 2:
                    string += "|"
            string += "\n"
            if x < 2:
                string += "-----\n"
        return string

    def play_move(self, x, y, player):
        if self.board[x][y] == 0:
            self.board[x][y] = player
            return True
        return False

    def _check_winner(self):

        for x in range(3):
            result = 1
            for y in range(3):
                result *= self.board[x][y]
            if result == 1:
                return 1
            elif result == 8:
                return 2
        for y in range(3):
            result = 1
            for x in range(3):
                result *= self.board[x][y]
            if result == 1:
                return 1
            elif result == 8:
                return 2
        result = 1
        for i in range(3):
            result *= self.board[i][i]
        if result == 1:
            return 1
        elif result == 8:
            return 2
        result = 1
        for i in range(3):
            result *= self.board[2-i][i]
        if result == 1:
            return 1
        elif result == 8:
            return 2
        return 0

    @staticmethod
    def page_clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def game_player(self):
        print(self._board_string())
        for turns in range(9):
            while True:
                x, y = input("x y >").split()
                x = int(x)
                y = int(y)
                if self.play_move(x, y, self.player):
                    print("wtf!!!!")
                    if self.player == 1:
                        self.player = 2
                    else:
                        self.player = 1
                    break
            print(self._board_string())
            if self._check_winner() != 0:
                print(f"player {self._check_winner()}")
                break
