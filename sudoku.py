
command_queue = []

class Board:
    def __init__(self, compacted=None):
        self.rows = []
        for row in range(9):
            self.rows.append([' ' for _ in range(9)])
        if compacted is not None and len(compacted) == 81:
            for row in range(9):
                for col in range(9):
                    self.rows[row][col] = compacted[row * 9 + col]

    def compact(self):
        srows = []
        for row in self.rows:
            srows.append("".join(row))
        return "".join(srows)

    def clear(self):
        self.rows = []
        for row in range(9):
            self.rows.append([' ' for _ in range(9)])
        
    def set(self, row, col, val):
        if val != ' ':
            if not self.can_take(row, col, val):
                raise ValueError(f"Cannot put {val} on ({row}, {col})")
        self.rows[row][col] = val

    def set_row(self, row, all_nums):
        for i in range(9):
            self.rows[row][i] = all_nums[i]

    def filled(self):
        for row in range(9):
            for col in range(9):
                if self.rows[row][col] == ' ':
                    return False
        return True

    def print(self):
        print("      1   2   3    4   5   6    7   8   9   ")
        print("   ++===+===+===++===+===+===++===+===+===++")
        for row in range(9):
            s = ' '+ chr(ord('A') + row) + ' ||'
            for col in range(9):
                s += ' ' + self.rows[row][col] + ' |'
                if col % 3 == 2:
                    s += '|'
            print(s)
            c = '=' if row % 3 == 2 else '-'
            print(f"   ++{c*3}+{c*3}+{c*3}++{c*3}+{c*3}+{c*3}++{c*3}+{c*3}+{c*3}++")

    def is_empty(self, row, col):
        return self.rows[row][col] == ' '

    def row_has(self, row, num):
        for col in range(9):
            if self.rows[row][col] == num:
                return True
        return False

    def col_has(self, col, num):
        for row in range(9):
            if self.rows[row][col] == num:
                return True
        return False

    def square_has(self, square_row, square_col, num):
        for row in range(3):
            for col in range(3):
                if self.rows[square_row * 3 + row][square_col * 3 + col] == num:
                    return True
        return False

    def can_take(self, row, col, num):
        if not self.is_empty(row, col):
            return False
        if self.row_has(row, num) or self.col_has(col, num) or self.square_has(row // 3, col // 3, num):
            return False
        return True

    def get_candidates(self, row, col):
        # get what digits can go to this square
        candidates = []
        for num in "123456789":
            if self.can_take(row, col, num):
                candidates.append(num)
        return candidates
            
    def rowcol(self, mnemonic):
        # convert a "a1" to [0,0]
        return [ ord(mnemonic[0].upper()) - ord('A'), int(mnemonic[1]) - 1 ]

    def mnem(self, row, col):
        return chr(ord('A') + row) + str(col + 1)

    def find_possible_numbers_for_each_cell(self, verbose=False):
        # for each square, see how many candidates exist
        # if only one candidate exists, say it
        possibles = []
        for row in range(9):
            for col in range(9):
                candidates = self.get_candidates(row, col)
                if len(candidates) == 1:
                    possibles.append(self.mnem(row, col) + "=" + candidates[0])
                if len(candidates) > 0 and verbose:
                    print(self.mnem(row, col) + ": " + ", ".join(candidates))
        return possibles
                    
    def find_unique_number_locations_per_3x3_square(self, verbose=False):
        # for each 3x3 square, find candidate squares for all numbers
        # if a number is only candidate in one location, propose this.
        possibles = []
        for square_row in range(3):
            for square_col in range(3):
                sq_num = square_row * 3 + square_col + 1
                for num in "123456789":
                    locs = []
                    for r in range(3):
                        for c in range(3):
                            if self.can_take(square_row * 3 + r, square_col * 3 + c, num):
                                locs.append(self.mnem(square_row * 3 + r, square_col * 3 + c))
                    if len(locs) == 1:
                        possibles.append(locs[0] + "=" + num)
                    if len(locs) > 0 and verbose:
                        print(f"Square {sq_num}, Num {num} can go to " + ", ".join(locs))
        return possibles

    def find_unique_number_locations_per_col(self, verbose=False):
        # for each column, find candidate squares for all numbers
        # if a number is only candidate in one location, propose this.
        possibles = []
        for col in range(9):
            for num in "123456789":
                locs = []
                for row in range(9):
                    if self.can_take(row, col, num):
                        locs.append(self.mnem(row, col))
                if len(locs) == 1:
                    possibles.append(locs[0] + "=" + num)
                if len(locs) > 0 and verbose:
                    print(f"Column {col + 1}, Num {num} can go to " + ", ".join(locs))
        return possibles

    def find_unique_number_locations_per_row(self, verbose=False):
        # for each row, find candidate squares for all numbers
        # if a number is only candidate in one location, propose this.
        possibles = []
        for row in range(9):
            for num in "123456789":
                locs = []
                for col in range(9):
                    if self.can_take(row, col, num):
                        locs.append(self.mnem(row, col))
                if len(locs) == 1:
                    possibles.append(locs[0] + "=" + num)
                if len(locs) > 0 and verbose:
                    print(f"Row {row + 1}, Num {num} can go to " + ", ".join(locs))
        return possibles



b = Board()
b.set_row(0, "      9  ")
b.set_row(1, "  9 43 8 ")
b.set_row(2, "3  7 1   ")
b.set_row(3, "    8   9")
b.set_row(4, "  5    6 ")
b.set_row(5, "46    5  ")
b.set_row(6, "  86   4 ")
b.set_row(7, " 5  7    ")
b.set_row(8, " 4 15 72 ")

b.set_row(0, "  48659  ")
b.set_row(1, "5 924368 ")
b.set_row(2, "386791 5 ")
b.set_row(3, " 3 586  9")
b.set_row(4, "895    6 ")
b.set_row(5, "46 9  5 8")
b.set_row(6, "  86 9 45")
b.set_row(7, "65  7 89 ")
b.set_row(8, "943158726")
b.print()


def execute(board, cmd):
    global verbose

    if cmd == '?':
        print("\tp   : print")
        print("\ta1=X: set number on row/col. enter no value after '=' to clear")
        print("\ta1  : get info on cell")
        print("\tq   : print command queue")
        print("\tqe  : execute all commands from queue")
        print("\tqc  : clear command queue")
        print("\tv   : toggle verbose")
        print("\tquit: quit")
    elif len(cmd) >= 3 and cmd[2] == '=':
        [row, col] = board.rowcol(cmd)
        val = cmd[3] if len(cmd) > 3 else ' '
        try:
            board.set(row, col, val)
            board.print()
        except Exception as e:
            print(str(e))
    elif len(cmd) == 2 and cmd[0].lower() in "abcdefghi" and cmd[1] in "123456789":
        [row, col] = board.rowcol(cmd)
        print(cmd.upper() + ": " + board.rows[row][col] + " - candidates: " + ", ".join(board.get_candidates(row, col)))
    elif cmd == 'clear':
        board.clear()
        board.print()
    elif cmd == 'p':
        board.print()
    elif cmd == 'a':
        possibles = board.find_possible_numbers_for_each_cell(verbose)
        if len(possibles) > 0:
            print("Got " + ", ".join(possibles))
            command_queue.extend(possibles)
    elif cmd == 'b':
        possibles = board.find_unique_number_locations_per_3x3_square(verbose)
        if len(possibles) > 0:
            print("Got " + ", ".join(possibles))
            command_queue.extend(possibles)
    elif cmd == 'c':
        possibles = board.find_unique_number_locations_per_col(verbose)
        if len(possibles) > 0:
            print("Got " + ", ".join(possibles))
            command_queue.extend(possibles)
    elif cmd == 'd':
        possibles = board.find_unique_number_locations_per_row(verbose)
        if len(possibles) > 0:
            print("Got " + ", ".join(possibles))
            command_queue.extend(possibles)
    elif cmd == 'q':
        print(f"{len(command_queue)} commands in queue")
        print("\n".join(command_queue))
    elif cmd == 'qe':
        for cmd in command_queue:
            execute(board, cmd)
        command_queue.clear()
    elif cmd == 'qc':
        command_queue.clear()
    elif cmd == 'v':
        verbose = not verbose
        print("Verbose is now " + ("on" if verbose else "off"))
    else:
        print("Don't understand... ?=help")

verbose=False
while True:
    prompt = f"({len(command_queue)} cmds) " if len(command_queue) > 0 else ""
    prompt += " > "
    cmd = input(prompt)
    if cmd == 'quit':
        break
    execute(b, cmd)



