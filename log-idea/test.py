

class Fact:
    # what is a fact? an undisputable piece of information
    def __init__(self) -> None:
        self.name = ""
        self.value = None


class Decision:
    # a decision is usually an answer to a question.
    # it can be boolean, a numeric value, a choice of a set, etc.
    # e.g. "umbrella? yes", "shelf: A2"
    def __init__(self) -> None:
        pass

class Driver:
    # a driver is the authority, role, or ego behind a fact, rule etc.
    # it asks questions of whether a decision can be overriden by another decision
    # the hierarchy of drivers, represent the decision making ethics.
    # i.e. will you prioritize the will of an employee over profit?

    def __init__(self) -> None:
        # for now, we can also add relations, i.e. "above that driver" etc
        self.level = 0

    def is_stronger_than(self, driver: Driver) -> bool:
        return False

class Condition:
    # could be anything, from hard coded true, to complex decision tree
    def __init__(self) -> None:
        pass

    def is_met(self):
        # we can evaluate the condition against known facts
        return False

class Nugget:
    # what is there in a nugget?
    def __init__(self, condition: Condition, decision, driver: Driver) -> None:
        self.condition = condition
        self.decision = decision
        self.driver = driver


class NuggerCollection:

    def __init__(self) -> None:
        self.nuggets = []

    def is_decision_valid(decision) -> Bool:
        return False

    def what_takes_to_make_decision(decision) -> Condition:
        # it can be an OR condition of alternative routes
        # essentially, all the possible graph paths that would enable the decision
        return []


statements = [
    "fact: it is raining",
    "fact: it is Tuesday",
    "if it is raining, then I will take umbrella or raincoat",
    "if it is windy, raincoat is preferred over umbrella",
    "if my car is out for service, I will take the bus",
    "if I take the bus, I need my Charliecard",
    "if I take the car, I can take a cup of coffee",
]

def get_next_line(lines, line_no) -> List[str, int]:
    # ignore empty lines and comments
    # see if line continues to next line indented

 
def parse_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if len(line) == 0 or line[0] == '#':
            continue
        # "it is <name>" ==> name = true
        # "it is not <name>" ==> name = false
        # "if <cond> then <blah>"
        # "unless <cond> then <blah>"
        # "<blah> if <cond>"
        # "<blah> unless <cond>"
        # heavy-item is item-weight > 150  <-- definition, using condition
        # raining is true   <-- definition using value
        # if heavy-item, then aisles 5-7
        # 

        

def run_test():
    # parse the file, load things into memory
    # can be hardcoded for now.
    # then try to deduce anything that can be deduced.
    # then, either allow query on those things,
    # or present them, so that new rules can be written on them etc.
    pass

print("Hello")

