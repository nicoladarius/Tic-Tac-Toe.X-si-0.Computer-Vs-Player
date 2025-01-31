""" Computerul va alege o pozitie random """

import random

class TicTacToe:
    def __init__(self):
        # Creăm tabla de joc
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # Jucătorul va juca cu X, iar computerul cu O

    def display_board(self):
        """Afișează tabla de joc cu numerotare pe coloane și linii și delimitare între celule."""
        print("\n  A   B   C")
        for i in range(3):
            # Afișăm linia corespunzătoare
            print(str(i + 1) + " " + " | ".join(self.board[i]))  # 1, 2, 3 pentru linii
            if i < 2:  # Adăugăm delimitator doar între linii
                print("  ---------")
        print("\n")

    def is_valid_move(self, move):
        """Verifică dacă mutarea este validă (adică celulele nu sunt ocupate)."""
        row, col = move
        return self.board[row][col] == ' '

    def make_move(self, player, move):
        """Plasează un simbol pe tablă."""
        row, col = move
        self.board[row][col] = player

    def check_winner(self):
        """Verifică dacă există un câștigător."""
        # Verificăm rânduri și coloane
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]

        # Verificăm diagonalele
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        # Verificăm egalitatea
        if all(cell != ' ' for row in self.board for cell in row):
            return 'Draw'

        return None  # Jocul continuă

    def get_computer_move(self):
        """Computerul face o mișcare aleatorie."""
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        return random.choice(empty_cells)

    def play_game(self):
        """Logica jocului între jucător și computer."""
        while True:
            # Afișăm tabla de joc
            self.display_board()

            # Mutarea jucătorului
            move = input("Introduceti mutarea (ex: A1, B2, C3): ").upper()
            if len(move) != 2 or move[0] not in "ABC" or move[1] not in "123":
                print("Mutare invalidă. Încearcă din nou.")
                continue

            col = "ABC".index(move[0])  # Convertim litera în coloană
            row = int(move[1]) - 1  # Convertim numărul în linie

            if not self.is_valid_move((row, col)):
                print("Această celulă este deja ocupată. Încearcă din nou.")
                continue

            # Jucătorul face mutarea
            self.make_move('X', (row, col))

            # Verificăm dacă jucătorul a câștigat
            winner = self.check_winner()
            if winner:
                self.display_board()
                if winner == 'X':
                    print("Ai câștigat!")
                elif winner == 'O':
                    print("Computerul a câștigat!")
                else:
                    print("Este egal!")
                break

            # Mutarea computerului
            print("Computerul face mutarea...")
            computer_move = self.get_computer_move()
            self.make_move('O', computer_move)

            # Verificăm dacă computerul a câștigat
            winner = self.check_winner()
            if winner:
                self.display_board()
                if winner == 'X':
                    print("Ai câștigat!")
                elif winner == 'O':
                    print("Computerul a câștigat!")
                else:
                    print("Este egal!")
                break

# Pornim jocul
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
