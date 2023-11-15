# idea of a logic compiler

Maybe in the direction of prolog etc.
The idea of a language, that can contain
facts and rules and spit out decisions.

The rules should be layered, as in for example
"this is the default" and "but we may also..."

Minimum knowledge should be needed for layering the rules,
it should be able to work with just small bits of info,
i.e. this rule is by a supervisor of mine, therefore
it is stronger than mine.

I guess a stupid example is "where do we put this box".
The rules should allow for options such as:

* Put them on shelves, I don't want them on the floor.
* If we can put them near the doors, it's better
* I prefer to push them on the lower shelves, it's faster
* This one is fragile, so it goes to aisles 5-6
* But at the momemt aisle 5 is blocked, so don't use it
* Since we have this urgent load, let's put everything to aisle 1 and reiterate.

## facts, rules

We need a way to state facts.

* it is raining, that's a Fact
* the truck is here, that's another fact.

We need a way to deduce things

* if it is raining, top speed allowed is 85% of the nominal, because it's the law
* if package is fragile, it has to go to aisles 5-6, because that's the policy
* if package is flammable, it can only go to zone F, because of Fire code

It seems each statement does this:

* if condition is satisfied in some way,
* add a new rule or fact
* and explain who drives this rule

Each statement has:

* A condition to be possibly met by other facts or rules
* A new fact or condition
* The driver of the fact or rule.

Drivers have hierarchy. For example, if a policy goes against the law
it's more important to abide to the law, than to perform an unlawful action.

## fun fact

I don't think we need a compiler for this, we need a program
that takes input from databases, streams, files, APIs,
and spits outputs in similar ways, in databases, stream, files, APIs.

Well.. we need a parser, to allow the language to be more natural.

The outputs are derived facts. Each one should be accompanied
by the facts and rules that derived them, essentially to explain
how they came to be.

## background

This idea came to be, because of all the crazy, 
conficting asks at the company I work for.
There are people who are driving one thing, 
but also people who are driving another thing.

Usually one of them is higher at the hierarchy, 
or we try to avoid collision, e.g. each to not step 
on the other's toes.

So, I was thinking, maybe I can put everything into a file,
run this program, and it will tell me what to do, 
or, which rules are creating conflict, and which drivers
have to tiebreak, to make a final decision.

Also, it's fun to play with such logic puzzles in real life,
people are not aware how unsentimental computers are.

