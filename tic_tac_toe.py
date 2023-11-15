# program to investigate tic-tac-toe solutions
import time
import random
from typing import List
import pdb

def breakpoint():
    pdb.set_trace()

def get(prompt, chars, default=None):
    while True:
        k = input(prompt)
        if k in chars:
            return k

class TTT:
    def __init__(self, compacted = None):
        self.matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        if compacted is not None and len(compacted) == 9:
            for i in range(9):
                self.matrix[int(i / 3)][int(i % 3)] = compacted[i]

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

    def compacted(self):
        s = ""
        for row in range(3):
            for col in range(3):
                s += '.' if self.matrix[row][col] == ' ' else self.matrix[row][col]
        return s

class Move:
    def __init__(self, row, col, symbol):
        self.row = row
        self.col = col
        self.symbol = symbol
        self.compacted = ''
        self.outcome = None
        self.children = []

    def __str__(self):
        return f"{self.symbol} @ ({self.row},{self.col}) --> {self.compacted}: {self.outcome}"

    def debug_string(self, prefix = ''):
        s = str(self)
        if len(self.children) > 0:
            s += "\n" + "\n".join([x.debug_string(prefix + '  ') for x in self.children])
        return s

    def count(self):
        return 1 + sum([child.count() for child in self.children])
    
    def is_winning_path(self):
        if self.outcome == 'win':
            return True
        for child in self.children:
            if child.is_winning_path():
                return True
        return False

    def get_winning_paths(self):
        # if self is win, we are the only move to win (we should have no children)
        if self.outcome == 'win':
            return [[self]]

        # gather winning children paths, prepend self before returning to caller
        winning_paths = []
        for child in self.children:
            paths = child.get_winning_paths()
            if len(paths) == 0:
                continue
            for path in paths:
                path.insert(0, self)
            winning_paths.extend(paths)

        return winning_paths

class Player:
    AI_RANDOM = 1
    AI_AVOID_LOSING = 2
    AI_WINNING = 3
    AI_WINNING_AVOID_LOSING = 4
    AI_SHORTEST_WIN = 5
    AI_AVOID_LOSING_SHORTEST_WIN = 5

    def __init__(self, name, symbol, intelligence=None):
        self.name = name
        self.symbol = symbol
        self.intelligence = intelligence
        self.other_player_symbol = 'O' if self.symbol == 'X' else 'X'

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
        if self.intelligence == self.AI_WINNING or self.intelligence == self.AI_WINNING_AVOID_LOSING: 
            [row, col] = self._get_winning_location(ttt)
            if row is not None and col is not None:
                print(f"{self.name} plays {self.symbol} at [{row},{col}] to win")
                ttt.play(row, col, self.symbol)
                return

        if self.intelligence in [self.AI_AVOID_LOSING, self.AI_WINNING_AVOID_LOSING, self.AI_AVOID_LOSING_SHORTEST_WIN]:
            locations = self._get_avoid_losing_locations(ttt)
            if len(locations) > 1:
                print(f"Argh, detected {len(locations)} possible losing locations...")
            if len(locations) > 0:
                row = locations[0][0]
                col = locations[0][1]
                print(f"{self.name} plays {self.symbol} at [{row},{col}] to avoid losing")
                ttt.play(row, col, self.symbol)
                return

        if self.intelligence == self.AI_SHORTEST_WIN:
            [row, col] = self._get_shortest_winning_location(ttt)
            if row is not None and col is not None:
                print(f"{self.name} plays {self.symbol} at [{row},{col}] as the shortest path to victory")
                ttt.play(row, col, self.symbol)
                return

        # falling back to random playing
        [row, col] = self._get_random_location(ttt)
        print(f"{self.name} plays {self.symbol} at [{row},{col}] at random")
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

    def _get_avoid_losing_locations(self, ttt):
        # try to see if other player will win if he played somewhere
        locations = []
        for row in range(3):
            for col in range(3):
                if not ttt.can_play(row, col):
                    continue
                ttt.play(row, col, self.other_player_symbol)
                would_win = ttt.has_won(self.other_player_symbol)
                ttt.clear(row, col)
                if would_win:
                    locations.append([row, col])
        return locations

    def _get_shortest_winning_location(self, ttt):
        # evaluate all possible solutions, starting with current board, get the most shallow onea
        print("Thinking...")
        moves = self._get_possible_moves(ttt, my_turn=True, depth=1)
        # then flatten the tree and find shallowest route to victory
        nodes_count = sum([move.count() for move in moves])
        print(f"Calculated {nodes_count} nodes in total")
        winning_paths = []
        for move in moves:
            winning_paths.extend(move.get_winning_paths())
        print(f"Calculated {len(winning_paths)} winning paths")
        shortest_path = None
        for path in winning_paths:
            if shortest_path is None or len(path) < len(shortest_path):
                shortest_path = path
        if shortest_path is None:
            return [None, None]
        print(f"Shortest path to win is {len(shortest_path)} steps")
        print("  " + "\n  ".join([str(move) for move in shortest_path]))
        return [shortest_path[0].row, shortest_path[0].col]
        

    def _get_possible_moves(self, ttt, my_turn, depth) -> List[Move]:
        empty_coords = ttt.get_empty_coords()
        if len(empty_coords) == 0:
            return []

        moves = []
        for coords in empty_coords:
            symbol = self.symbol if my_turn else self.other_player_symbol
            move = Move(coords[0], coords[1], symbol)
            ttt.play(coords[0], coords[1], symbol)
            move.compacted = ttt.compacted()
            won = ttt.has_won(symbol)
            if won:
                move.outcome = 'win' if my_turn else 'lose'
            else:
                move.children = self._get_possible_moves(ttt, not my_turn, depth + 1)
                if len(move.children) == 0:
                    move.outcome = 'tie'
            ttt.clear(coords[0], coords[1])
            moves.append(move)
        return moves



def get_players():
    print("1 - human vs human")
    print("2 - human vs computer (human starts)")
    print("3 - computer vs human (computer starts)")
    print("4 - computer vs computer")
    print("0 - quit")
    gt = get("Choose game type: ", '12340q')
    if gt in '0qQ':
        return None

    if gt in '234':
        print("1 - random")
        print("2 - avoid losing")
        print("3 - winning")
        print("4 - winning, then avoid losing")
        print("5 - shortest path to victory")
        print("6 - avoid losing, then shortest path to victory")
        it = get("Choose intelligence type: ", "123456")

    intelligences = [
        Player.AI_RANDOM,
        Player.AI_AVOID_LOSING,
        Player.AI_WINNING,
        Player.AI_WINNING_AVOID_LOSING,
        Player.AI_SHORTEST_WIN,
        Player.AI_AVOID_LOSING_SHORTEST_WIN,
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


