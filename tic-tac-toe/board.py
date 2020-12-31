
class Board:
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

