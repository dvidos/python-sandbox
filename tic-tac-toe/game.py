from tools import get
from board import Board
from player import Player

def get(prompt, chars, default=None):
    while True:
        k = input(prompt)
        if k in chars:
            return k

class Game:

    def get_players(self):
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
        else:
            ai = None

        configurations = [
            [Player('Human 1', 'X'), Player('Human 2', 'O')],
            [Player('Human', 'X'), Player('Computer', 'O', ai)],
            [Player('Computer', 'X', ai), Player('Human', 'O') ],
            [Player('Zarg', 'X', ai), Player('Fizz', 'O', ai)],
        ]

        return configurations[int(gt) - 1]

    def play_game(self, players):
        board = Board()
        board.print()
        player = 0
        while True:
            players[player].move(board)

            board.print()
            for p in range(2):
                if board.has_won(players[p].symbol):
                    print(f"{players[p].name} won!")
                    return
            if board.is_finished():
                print("It's a tie!")
                return

            player = (player + 1) % 2
        
    def run(self):
        while True:
            players = self.get_players()
            if players == None:
                break
            print("")
            self.play_game(players)


