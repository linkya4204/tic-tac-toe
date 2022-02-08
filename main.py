import random


class TicTacToe:
    def __init__(self):
        self.board = []
        self.is_continue = True
        self.first_player = random.choice(["X", "O"])
        self.second_player = "O" if self.first_player == "X" else "X"

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("_")
            self.board.append(row)
        return self.board

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()  # print nothing, use to do the next line


    def check_win(self,player):
        row_list = []
        for row in self.board:
            row_list.append(all(item ==player for item in row))

        col_list_sum = []
        for i in range(0,3):
            col_list = []
            for row in self.board:
                col_list.append(row[i])
            col_list_sum.append(all(item ==player for item in col_list))


        cross_1 =[self.board[0][0],self.board[1][1],self.board[2][2]]
        cross_2 = [self.board[0][2], self.board[1][1], self.board[2][0]]

        if any(row_list) or any(col_list_sum) or all(item ==player for item in cross_1) or all(item ==player for item in cross_2):
            print(f'Player {player} wins the game!')
            return False
        else:
            return True

    def board_fill(self):
        row_list = []
        for row in self.board:
            for item in row:
                row_list.append(item)
        if all(item !="_" for item in row_list):
            print('Match Draw!')
            return False
        else:
            return True

    def check_avai(self,row_num,col_num,player):
        if self.board[row_num][col_num] !="_":
            print('You cannot put the mark here.')
            self.player_turn(player)
        else:
            self.board[row_num][col_num] = player

    def player_turn(self,player):
        print()
        print(f"Player {player} turn")
        user_input = input('Enter your fixed spot:')
        row_num = int(user_input[0]) - 1
        col_num = int(user_input[1]) - 1
        self.check_avai(row_num,col_num,player)


    def check_continue(self,player):
        self.show_board()
        self.is_continue = self.check_win(player)
        if self.is_continue == True:
            self.is_continue = self.board_fill()

    def start_game(self):
        guide = "Guide: Enter row and column numbers to fix spot (ie.12,23) \n" \
                "Don't input number of row or column larger than 3 such as 14 or 41."
        print(guide)
        self.create_board()
        self.show_board()
        while self.is_continue:
            self.player_turn(self.first_player)
            self.check_continue(self.first_player)
            if self.is_continue == False:
                self.show_board()
                break
            else:
                self.player_turn(self.second_player)
                self.check_continue(self.second_player)



game = TicTacToe()
game.start_game()




