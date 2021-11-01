import os
import random


class TicTacToe:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.player = 1
        self.gametype = 0

    def menu(self):
        string = "Welcome to TicTacToe\n" + \
                 "Choose one of the following options:\n" + \
                 "v: To play versus another player\n" + \
                 "c: To play versus a random CPU\n" + \
                 "q: to quit\n"

        self.page_clear()
        print(string)
        user_choice = input(">")
        if user_choice == "q":
            return
        elif user_choice == "v":
            self.game_player()
        elif user_choice == "c":
            self.game_random(random.randint(1, 2))

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
        for i in range(3):
            if self.board[i][0] != 0 and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            if self.board[2][i] != 0 and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        if self.board[0][0] != 0 and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return self.board[1][1]
        if self.board[0][2] != 0 and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return self.board[1][1]
        return 0

    def _board_is_full(self):
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == 0:
                    return False
        return True

    @staticmethod
    def page_clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def game_player(self):
        self.page_clear()
        print(self._board_string())
        while not self._board_is_full():
            while True:
                user_input = input(
                    f"player{self.player}'s turn\nx for vertical y for horizontal starting at top left or q to quit\nx y >")
                if user_input == "q":
                    return
                try:
                    x, y = user_input.split()
                    x = int(x)
                    y = int(y)
                    if self.play_move(x, y, self.player):
                        if self.player == 1:
                            self.player = 2
                        else:
                            self.player = 1
                        break
                    else:
                        print("Invalid Input")
                except:
                    print("Invalid Input")
            self.page_clear()
            print(self._board_string())
            if self._check_winner() != 0:
                break
        if self._check_winner() != 0:
            print(f"PLAYER {self._check_winner()} WINS!!!")

        else:
            print(f"TIE!!")
        print("Press ENTER to quit")
        input()

    def move_random(self, player_cpu):
        while True:
            cpu_x = random.randint(0, 2)
            cpu_y = random.randint(0, 2)
            if self.play_move(cpu_x, cpu_y, player_cpu):
                break

    def game_random(self, player_cpu):
        if player_cpu == 1:
            player_human = 2
        else:
            player_human = 1
        self.page_clear()
        print(self._board_string())
        while not self._board_is_full():
            if self.player == player_human:
                while True:
                    user_input = input(
                        f"x for vertical y for horizontal starting at top left or q to quit\nx y >")
                    if user_input == "q":
                        return
                    try:
                        x, y = user_input.split()
                        x = int(x)
                        y = int(y)
                        if self.play_move(x, y, player_human):
                            break
                        else:
                            print("Invalid Input")
                    except:
                        print("Invalid Input")
            elif self.player == player_cpu:
                self.move_random(player_cpu)
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1
            self.page_clear()
            print(self._board_string())
            if self._check_winner() != 0:
                break
        if self._check_winner() == player_human:
            print("Player Won!!!")
        elif self._check_winner() == player_cpu:
            print("CPU WON!!!")
        else:
            print(f"TIE!!")
        print("Press ENTER to quit")
        input()


    def move_best(self,player_max, player_min):
        best_move = [player_min,(0,0)]
        for x in range(3):
            for y in range(3):
                if self.play_move(x, y, player_max):
                    if self._check_winner() == player_max:
                        return [player_max,(x,y)]
                    elif self._check_winner() == player_min:
                        return [player_min,(x,y)]
                    elif self._board_is_full():
                        return [0, (x, y)]
                    best_move = self.move_best(player_min,player_max)


    def game_perfect(self, player_cpu):
        if player_cpu == 1:
            player_human = 2
        else:
            player_human = 1
        self.page_clear()
        print(self._board_string())
        for turns in range(9):
            if self.player == player_human:
                while True:
                    user_input = input(
                        f"x for vertical y for horizontal starting at top left or q to quit\nx y >")
                    if user_input == "q":
                        return
                    try:
                        x, y = user_input.split()
                        x = int(x)
                        y = int(y)
                        if self.play_move(x, y, player_human):
                            break
                        else:
                            print("Invalid Input")
                    except:
                        print("Invalid Input")
            elif self.player == player_cpu:
                self.move_random(player_cpu)
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1
            self.page_clear()
            print(self._board_string())
            if self._check_winner() != 0:
                break
        if self._check_winner() == player_human:
            print("Player Won!!!")
        elif self._check_winner() == player_cpu:
            print("CPU WON!!!")
        else:
            print(f"TIE!!")
        print("Press ENTER to quit")
        input()