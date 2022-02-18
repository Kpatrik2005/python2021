import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            sor = []
            for j in range(3):
                sor.append('-')
            self.board.append(sor)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, sor, col, player):
        self.board[sor][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking sors
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for sor in self.board:
            for item in sor:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for sor in self.board:
            for item in sor:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for sor in self.board:
            for item in sor:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            sor, col = list(
                map(int, input("Adja meg a sor- és oszlopszámokat a pont javításához: ").split()))
            print()

            # fixing the spot
            self.fix_spot(sor - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()


python tictactoe2.py 
Player X turn
- - -
- - -
- - -
Enter row and column numbers to fix spot: 1 1

Player O turn
X - -
- - -
- - -
Enter row and column numbers to fix spot: 2 1

Player X turn
X - -
O - -
- - -
Enter row and column numbers to fix spot: 1 2

Player O turn
X X -
O - -
- - -
Enter row and column numbers to fix spot: 1 3

Player X turn
X X O
O - -
- - -
Enter row and column numbers to fix spot: 2 2

Player O turn
X X O
O X -
- - -
Enter row and column numbers to fix spot: 3 3

Player X turn
X X O        
O X -        
- - O
Enter row and column numbers to fix spot: 3 2

Player X wins the game!

X X O
O X -
- X O
