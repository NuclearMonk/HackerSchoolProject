class TicTacToe:
    def __init__(self):
        self.board = [[2 for _ in range(3)] for _ in range(3)]

    def board_string(self):
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
