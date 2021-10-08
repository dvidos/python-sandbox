import time


a = [
    [ 1, 0, 0, 0, 0, 0 ],
    [ 0, 1, 0, 1, 1, 1 ],
    [ 0, 0, 1, 0, 1, 0 ],
    [ 1, 1, 0, 0, 1, 0 ],
    [ 1, 0, 1, 1, 0, 0 ],
    [ 1, 0, 0, 0, 0, 1 ]
]

# let's build a tree of dependencies, each cell with have either true (edge/1), false (zero) or unknown dependencies
# then, as we solve each one, we'll update each cell's dependencies. if one dependency is an island, the cell is an island.
class CellInfo:
    def __init__(self):
        self.island = False
        self.certain = False
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def __repr__(self):
        s = ""
        if self.certain:
            s += "1" if self.island else "0"
        else:
            s += "?"
        s += "-"
        if self.north is not None:
            s += "N"
        if self.south is not None:
            s += "S"
        if self.east is not None:
            s += "E"
        if self.west is not None:
            s += "W"
        return s

    def has_certain_neighboring_island(self):
        for neighbor in [self.north, self.south, self.east, self.west]:
            if neighbor is not None and neighbor.certain and neighbor.island:
                return True
        return False



def build_dependencies():
    global a
    dependencies = {}
    # initial creation
    for row in range(6):
        for col in range(6):
            key = str(row) + "-" + str(col)
            d = CellInfo()
            if row == 0 or row == 5 or col == 0 or col == 5:
                d.island = a[row][col] == 1
                d.certain = True
            elif a[row][col] == 0:
                d.island = False
                d.certain = True
            dependencies[key] = d

    # now, cross link
    for row in range(6):
        for col in range(6):
            key = str(row) + "-" + str(col)
            if row > 0:
                dependencies[key].north = dependencies[str(row - 1) + "-" + str(col)]
            if row < 5:
                dependencies[key].south = dependencies[str(row + 1) + "-" + str(col)]
            if col > 0:
                dependencies[key].west = dependencies[str(row) + "-" + str(col - 1)]
            if col < 5:
                dependencies[key].east = dependencies[str(row) + "-" + str(col + 1)]

    return dependencies


def are_dependencies_solved(dependencies):
    for row in range(6):
        for col in range(6):
            key = str(row) + "-" + str(col)
            if not dependencies[key].certain:
                return False
    return True

def solve_dependencies_once(dependencies):
    updated = False
    for row in range(6):
        for col in range(6):
            key = str(row) + "-" + str(col)
            d = dependencies[key]
            if not d.certain and d.has_certain_neighboring_island():
                d.certain = True
                d.island = True
                updated = True
    return updated


def print_input():
    global a
    for row in range(6):
        s = "["
        for col in range(6):
            s += str(a[row][col]) + ", "
        s += "]"
        print(s)
    print("")

def print_dependencies(dependencies):
    for row in range(6):
        s = "["
        for col in range(6):
            key = str(row) + "-" + str(col)
            d = dependencies[key]
            if d.certain:
                s += "1" if d.island else "0"
            else:
                s += "?"
            s += ", "
        s += "]"
        print(s)


def run():
    print("Input")
    print_input()
    deps = build_dependencies()
    print_dependencies(deps)
    while True:
        print("Not solved yet, trying another pass");
        updated = solve_dependencies_once(deps)
        if not updated:
            break
        print_dependencies(deps)

run()
