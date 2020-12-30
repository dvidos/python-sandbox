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

    def is_finished(self):
        for row in range(3):
            for col in range(3):
                if self.matrix[row][col] == ' ':
                    return False
        return True

    def can_play(self, row, col):
        return self.matrix[row][col] == ' '

    def play(self, row, col, c):
        if c != ' ' and self.matrix[row][col] != ' ':
            raise RuntimeError(f"Cannot play at {row}, {col}, it is already taken")
        self.matrix[row][col] = c

    def clear(self, row, col):
        self.matrix[row][col] = ' '

    def clear_all(self):
        for row in range(3):
            for col in range(3):
                self.matrix[row][col] = ' '
        
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


class Player:
    AI_RANDOM = 1
    AI_AVOID_LOSING = 2
    AI_WINNING = 3

    def __init__(self, name, symbol, intelligence=None):
        self.name = name
        self.symbol = symbol
        self.intelligence = intelligence

    def move(self, ttt: TTT):
        if self.intelligence == None:
            self._move_human(ttt)
        else:
            self._move_computer(ttt)

    def _move_human(self, ttt: TTT):
        while True:
            k = get(f"{self.name} enter location to play (1-9): ", '123456789')
            row = int((int(k)-1) / 3)
            col = int((int(k)-1) % 3)
            if not ttt.can_play(row, col):
                print("Cannot play there")
                continue
            ttt.play(row, col, self.symbol)
            break
    
    def _move_computer(self, ttt: TTT):
        if self.intelligence == self.AI_WINNING:
            [row, col] = self._get_winning_location(ttt)
            if row is not None and col is not None:
                print(f"{self.name} plays at [{row},{col}] to win")
                ttt.play(row, col, self.symbol)
                return

        if self.intelligence == self.AI_AVOID_LOSING:
            [row, col] = self._get_avoid_losing_location(ttt)
            if row is not None and col is not None:
                print(f"{self.name} plays at [{row},{col}] to avoid losing")
                ttt.play(row, col, self.symbol)
                return

        # falling back to random playing
        [row, col] = self._get_random_location(ttt)
        print(f"{self.name} plays at [{row},{col}] at random")
        ttt.play(row, col, self.symbol)
    
    def _get_random_location(self, ttt):
        while True:
            r = random.randrange(9)
            row = int(r / 3)
            col = int(r % 3)
            if not ttt.can_play(row, col):
                continue
            return [row, col]
   
    def _get_winning_location(self, ttt):
        # try to see if a location will win us the game
        for row in range(3):
            for col in range(3):
                if not ttt.can_play(row, col):
                    continue
                ttt.play(row, col, self.symbol)
                would_win = ttt.has_won(self.symbol)
                ttt.clear(row, col)
                if would_win:
                    return [row, col]
        return [None, None]

    def _get_avoid_losing_location(self, ttt):
        # try to see if other player will win if he played somewhere
        other_player_symbol = 'X' if self.symbol == 'O' else 'O'
        for row in range(3):
            for col in range(3):
                if not ttt.can_play(row, col):
                    continue
                ttt.play(row, col, other_player_symbol)
                would_win = ttt.has_won(other_player_symbol)
                ttt.clear(row, col)
                if would_win:
                    return [row, col]
        return [None, None]

def get_players():
    print("1 - human vs human")
    print("2 - human vs computer (human starts)")
    print("3 - computer vs human (computer starts)")
    print("4 - computer vs computer")
    print("0 - exit")
    gt = get("Choose game type: ", '12340')
    if gt == '0':
        return None

    if gt in '234':
        print("1 - random")
        print("2 - avoid losing")
        print("3 - winning")
        it = get("Choose intelligence type: ", "123")

    intelligences = [
        Player.AI_RANDOM,
        Player.AI_AVOID_LOSING,
        Player.AI_WINNING,
    ]
    ai = intelligences[int(it) - 1]

    configurations = [
        [Player('Human 1', 'X'), Player('Human 2', 'O')],
        [Player('Human', 'X'), Player('Computer', 'O', ai)],
        [Player('Computer', 'X', ai), Player('Human', 'O') ],
        [Player('Zarg', 'X', ai), Player('Fizz', 'O', ai)],
    ]

    return configurations[int(gt) - 1]

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
    

while True:
    players = get_players()
    if players == None:
        break
    print("")
    play_game(players)


