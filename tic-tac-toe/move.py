

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

