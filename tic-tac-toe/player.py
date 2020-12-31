import random
from tools import get
from typing import List
from board import Board
from move import Move


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

    def move(self, board: Board):
        if self.intelligence == None:
            self._move_human(board)
        else:
            self._move_computer(board)

    def _move_human(self, board: Board):
        while True:
            k = get(f"{self.name} enter location to play (1-9): ", '123456789')
            row = int((int(k)-1) / 3)
            col = int((int(k)-1) % 3)
            if not board.can_play(row, col):
                print("Cannot play there")
                continue
            board.play(row, col, self.symbol)
            break
    
    def _move_computer(self, board: Board):
        if self.intelligence == self.AI_WINNING or self.intelligence == self.AI_WINNING_AVOID_LOSING: 
            [row, col] = self._get_winning_location(board)
            if row is not None and col is not None:
                print(f"{self.name} plays {self.symbol} at [{row},{col}] to win")
                board.play(row, col, self.symbol)
                return

        if self.intelligence in [self.AI_AVOID_LOSING, self.AI_WINNING_AVOID_LOSING, self.AI_AVOID_LOSING_SHORTEST_WIN]:
            locations = self._get_avoid_losing_locations(board)
            if len(locations) > 1:
                print(f"Argh, detected {len(locations)} possible losing locations...")
            if len(locations) > 0:
                row = locations[0][0]
                col = locations[0][1]
                print(f"{self.name} plays {self.symbol} at [{row},{col}] to avoid losing")
                board.play(row, col, self.symbol)
                return

        if self.intelligence == self.AI_SHORTEST_WIN:
            [row, col] = self._get_shortest_winning_location(board)
            if row is not None and col is not None:
                print(f"{self.name} plays {self.symbol} at [{row},{col}] as the shortest path to victory")
                board.play(row, col, self.symbol)
                return

        # falling back to random playing
        [row, col] = self._get_random_location(board)
        print(f"{self.name} plays {self.symbol} at [{row},{col}] at random")
        board.play(row, col, self.symbol)
    
    def _get_random_location(self, board):
        while True:
            r = random.randrange(9)
            row = int(r / 3)
            col = int(r % 3)
            if not board.can_play(row, col):
                continue
            return [row, col]
   
    def _get_winning_location(self, board):
        # try to see if a location will win us the game
        for row in range(3):
            for col in range(3):
                if not board.can_play(row, col):
                    continue
                board.play(row, col, self.symbol)
                would_win = board.has_won(self.symbol)
                board.clear(row, col)
                if would_win:
                    return [row, col]
        return [None, None]

    def _get_avoid_losing_locations(self, board):
        # try to see if other player will win if he played somewhere
        locations = []
        for row in range(3):
            for col in range(3):
                if not board.can_play(row, col):
                    continue
                board.play(row, col, self.other_player_symbol)
                would_win = board.has_won(self.other_player_symbol)
                board.clear(row, col)
                if would_win:
                    locations.append([row, col])
        return locations

    def _get_shortest_winning_location(self, board):
        # evaluate all possible solutions, starting with current board, get the most shallow onea
        print("Thinking...")
        moves = self._get_possible_moves(board, my_turn=True, depth=1)
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
        

    def _get_possible_moves(self, board, my_turn, depth) -> List[Move]:
        empty_coords = board.get_empty_coords()
        if len(empty_coords) == 0:
            return []

        moves = []
        for coords in empty_coords:
            symbol = self.symbol if my_turn else self.other_player_symbol
            move = Move(coords[0], coords[1], symbol)
            board.play(coords[0], coords[1], symbol)
            move.compacted = board.compacted()
            won = board.has_won(symbol)
            if won:
                move.outcome = 'win' if my_turn else 'lose'
            else:
                move.children = self._get_possible_moves(board, not my_turn, depth + 1)
                if len(move.children) == 0:
                    move.outcome = 'tie'
            board.clear(coords[0], coords[1])
            moves.append(move)
        return moves


