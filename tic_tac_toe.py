import random

print("Úgy tudsz mezőt kiválasztani, hogy előszőr megadod az oszlopszámot és utána a sorszámot ezt szóközel elválasztva")
class TicTacToe:
    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            sor = []
            for j in range(3):
                sor.append('-')
            self.board.append(sor)

    def get_random_first_jatekos(self):
        return random.randint(0, 1)

    def fix_spot(self, sor, col, jatekos):
        self.board[sor][col] = jatekos

    def is_jatekos_win(self, jatekos):
        win = None

        n = len(self.board)

        # sor ellenőrzése
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != jatekos:
                    win = False
                    break
            if win:
                return win

        # oszlopok ellenőrzése
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != jatekos:
                    win = False
                    break
            if win:
                return win

        # átlók ellenőrzése
        win = True
        for i in range(n):
            if self.board[i][i] != jatekos:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != jatekos:
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

    def swap_jatekos_turn(self, jatekos):
        return 'X' if jatekos == 'O' else 'O'

    def show_board(self):
        for sor in self.board:
            for item in sor:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        jatekos = 'X' if self.get_random_first_jatekos() == 1 else 'O'
        while True:
            print(f"jatekos {jatekos} köre")

            self.show_board()

            # felhasználói bevitel fogadása
            sor, col = list(
                map(int, input("Adja meg a sor- és oszlopszámokat a pont javításához: ").split()))
            print()

            # a hely rögzítése
            self.fix_spot(sor - 1, col - 1, jatekos)

            # annak ellenőrzése, hogy az aktuális jatekos nyert-e vagy sem
            if self.is_jatekos_win(jatekos):
                print(f"Játékos {jatekos} nyerte a játékot!")
                break

            # annak ellenőrzése, hogy a játék döntetlen-e vagy sem
            if self.is_board_filled():
                print("Döntetlen!")
                break

            # játékost cserélni
            jatekos = self.swap_jatekos_turn(jatekos)

        # a tábla végső nézetét mutatja
        print()
        self.show_board()


# a játék elindítása
ujra = "i"
while ujra == "i":
    ism = 1
    while ism < 4:
        tic_tac_toe = TicTacToe()
        tic_tac_toe.start()
        ism += 1
    ujra = input("Új játék(i/n)")


