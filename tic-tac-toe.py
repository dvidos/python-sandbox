# program to investigate tic-tac-toe solutions
import time
import random

def get(prompt, chars, default=None):
    while True:
        k = input(prompt)
        if k in chars:
            return k

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
    
class Player:
    AI_RANDOM = 1

    def __init__(self, name, symbol, intelligence=None):
        self.name = name
        self.symbol = symbol
        self.intelligence = intelligence

    def move(self, ttt: TTT):
        if self.intelligence == None:
            self._move_human(ttt)
        elif self.intelligence == self.AI_RANDOM:
            self._move_computer_random(ttt)

    def _move_human(self, ttt: TTT):
        while True:
            k = get(f"{self.name} enter location to play (1-9): ", '123456789')
            row = int((int(k)-1) / 3)
            col = int((int(k)-1) % 3)
            if not ttt.can_play(row, col):
                print("Cannot play there")
                continue
            ttt.play([row, col], self.symbol)
            break

    def _move_computer_random(self, ttt: TTT):
        while True:
            r = random.randrange(9)
            row = int(r / 3)
            col = int(r % 3)
            if not ttt.can_play(row, col):
                continue
            print(f"Computer plays at {r+1}")
            ttt.play([row, col], self.symbol)
            break



def play_game(players):
    ttt = TTT()
    ttt.print()
    player = 0
    while True:
        players[player].move(ttt)

        ttt.print()
        for p in range(2):
            if ttt.has_won(players[p].symbol):
                print(f"{players[p].name} won!")
                return
        if ttt.is_finished():
            print("It's a tie!")
            return

        player = (player + 1) % 2
    

print("1 - human vs human")
print("2 - human vs computer (human starts)")
print("3 - computer vs human (computer starts)")
print("4 - computer vs computer")
t = get("Choose game type: ", '1234')
ai = Player.AI_RANDOM  # we'll make this configurable later
configurations = [
    [Player('Human 1', 'X'), Player('Human 2', 'O')],
    [Player('Human', 'X'), Player('Computer', 'O', ai)],
    [Player('Computer', 'X', ai), Player('Human', 'O') ],
    [Player('Computer 1', 'X', ai), Player('Computer 2', 'O', ai)],
]
players = configurations[int(t) - 1]
play_game(players)


