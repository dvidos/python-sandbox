# 3.7 and later: from __future__ import annotations
from typing import List, Union, Tuple
import collections
import pdb
from hashlib import md5


# functional programming is a paradigm that 
# - avoids side effects by performing computations mainly by evaluation of functions
# - relies heavily on immutable data structures 
# one good outcome, one can do parallel programming without needing to lock the data,
#     as everything is read only.
# another one, as changes are represented in new immutable structures, we can use 
#     these new structures as history of what changed and when. CQRS anyone?
# 


# in F# most types are options (one of, uses OR) or structures with many attributes (composed, uses AND)
# in functinal programming, we have types, instead of objects. Types can also be lists of functions.
# each function has some inputs and some outputs. they both can be lists of functions for example.


# list of people, scientists, with properties (Name, born, field, nobel prize y/n)
# normally a list of dictionaries. but this is mutable (and without validations!)

# for immutable objects, he does a named tuple
Scientist = collections.namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])
# this creates a readonly named tuple that we can construct and see with pprint, but cannot change.
# to avoid having the list of scientists mutable, he creates a tuple! "(" instead of "["
scientists = (
    Scientist(name='Marie Curie', field='physics', born=1882, nobel=True),
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    # ...
)
# then he'll look into the filter(), map() and reduce() functions.



class Facts:
    
    def __init__(self, **kwargs):
        self._dict = kwargs

    def has(self, name: str):
        return name in self._dict

    def get(self, name: str):
        return self._dict[name] if name in self._dict else None

    def set(self, name: str, value) -> 'Facts':
        new_dict = self._dict.copy()
        new_dict[name] = value
        return Facts(**new_dict)
    
    def __str__(self):
        return str(self._dict)

    def hash(self):
        # pdb.set_trace()
        return md5(str(self._dict).encode()).hexdigest()


class Rule:
    def __init__(self, conditions = None, actions = None):
        self._conditions = []
        self._actions = []

        if conditions is not None:
            self._conditions = conditions if isinstance(conditions, list) else [conditions]

        if actions is not None:
            self._actions = actions if isinstance(actions, list) else [actions]

    def applies(self, facts: Facts) -> bool:
        if len(self._conditions) == 0:
            return False

        for condition in self._conditions:
            if not condition(facts):
                return False

        return True

    def act(self, facts: Facts) -> Facts:
        if len(self._actions) == 0:
            return facts

        for action in self._actions:
            facts = action(facts)

        return facts



def run_rules_engine(facts: Facts, rules: List[Rule]) -> Facts:
    facts_changed = True
    while facts_changed:
        print("Running all rules...")
        
        before = facts.hash()
        for rule in rules:
            if rule.applies(facts):
                facts = rule.act(facts)
        
        after = facts.hash()
        facts_changed = after != before

    return facts


# map()
# filter()
# reduce()


if __name__ == "__main__":
    facts = Facts(people=['john'])
    rules = []
    rules.append(Rule(
        lambda facts: facts.has("dog"),
        lambda facts: facts.set("need", "leash")
    ))
    rules.append(Rule(
        lambda facts: facts.has("people") and facts.get("people") == ['john'],
        lambda facts: facts.set("dog", "fido")
    ))

    """
    Initial facts: {'people': ['john']}
    Running all rules...
    Running all rules...
    Running all rules...
    Final facts: {'people': ['john'], 'dog': 'fido', 'need': 'leash'}
    """
    print("Initial facts: " + str(facts))
    final_facts = run_rules_engine(facts, rules)
    print("Final facts: " + str(final_facts))


