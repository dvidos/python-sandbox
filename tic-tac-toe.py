# program to investigate tic-tac-toe solutions
import time



class TTT:
    def __init__(self):
        self.matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player1 = True

    def print(self):
        print(f"   {self.matrix[0][0]} | {self.matrix[0][1]} | {self.matrix[0][2]} ")
        print("  ---+---+---")
        print(f"   {self.matrix[1][0]} | {self.matrix[1][1]} | {self.matrix[1][2]} ")
        print("  ---+---+---")
        print(f"   {self.matrix[2][0]} | {self.matrix[2][1]} | {self.matrix[2][2]} ")

    def clear(self):
        for row in range(3):
            for col in range(3):
                self.matrix[row][col] = ' '
        
    def is_finished(self):
        for row in range(3):
            for col in range(3):
                if self.matrix[row][col] == ' ':
                    return False
        return True

    def can_play(self, row, col):
        return self.matrix[row][col] == ' '

    def has_won(self, c):
        for row in range(3):
            if self.matrix[row][0] == c and self.matrix[row][1] == c and self.matrix[row][2] == c:
                return True

        for col in range(3):
            if self.matrix[0][col] == c and self.matrix[1][col] == c and self.matrix[2][col] == c:
                return True

        # diagonals
        if self.matrix[0][0] == c and self.matrix[1][1] == c and self.matrix[2][2] == c:
            return True
        if self.matrix[0][2] == c and self.matrix[1][1] == c and self.matrix[2][0] == c:
            return True

        return False

    def get_empty_coords(self):
        coords = []
        for row in range(3):
            for col in range(3):
                if self.matrix[row][col] == ' ':
                    coords.append([row, col])
        return coords
                
    def play(self, coords, c):
        if c != ' ' and self.matrix[coords[0]][coords[1]] != ' ':
            raise RuntimeError(f"Cannot play at {coords}, it is already taken")
        self.matrix[coords[0]][coords[1]] = c

    def test_recursively(self):
        for letter in ['X', 'O']:
            if self.has_won(letter):
                print(f"{letter} wins!")
                self.print()
                return
        
        coords = self.get_empty_coords()
        if len(coords) == 0:
            print(f"It's a tie")
            self.print()
            return

        for c in coords:
            letter = 'X' if self.player1 else 'O'
            print(f"Player {letter} plays at {c}...")
            self.play(c, letter)
            self.player1 = not self.player1
            # self.print()
            # time.sleep(.075)
            self.test_recursively()
            self.play(c, ' ')
    
def get(prompt, chars, default=None):
    while True:
        k = input(prompt)
        if k in chars:
            return k

class Player:
    def __init__(self, name, symbol, is_user=True):
        self.name = name
        self.symbol = symbol
        self.is_user = is_user


ttt = TTT()
ttt.print()
player = 0
players = ['Νικόλας', 'Μπαμπάς']
while True:
    k = get(f"Player {players[player]} enter location to play (1-9): ", '123456789')
    row = int((int(k)-1) / 3)
    col = int((int(k)-1) % 3)
    c = 'X' if player == 0 else 'O'
    if ttt.can_play(row, col):
        ttt.play([row, col], c)
        player = 1 if player == 0 else 0
    else:
        print("Cannot play there")

    ttt.print()

    if ttt.has_won('X'):
        print(f"{players[0]} won!")
        break

    if ttt.has_won('O'):
        print(f"{players[1]} won!")
        break

    if ttt.is_finished():
        print("It's a tie!")
        break




