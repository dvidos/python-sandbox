
# Tic Tac Toe

A game to investigate recursive trees and decisions into a (hopefully) fun game.

Game modes include:

* Human vs Human
* Human vs Computer
* Computer vs Computer

When computer plays, intelligence algorithms include:

* Random playing
* Prioritizing completing triplet to win
* Prioritizing avoiding losing
* Shortest path to wining of all available winning paths

etc.

To execute, in a shell run the following:

```bash
python ttt.py
```

Sample output

```
$ python ttt.py
1 - human vs human
2 - human vs computer (human starts)
3 - computer vs human (computer starts)
4 - computer vs computer
0 - quit
Choose game type: 2
1 - random
2 - avoid losing
3 - winning
4 - winning, then avoid losing
5 - shortest path to victory
6 - avoid losing, then shortest path to victory
Choose intelligence type: 6

     |   |
  ---+---+---
     |   |
  ---+---+---
     |   |
Human enter location to play (1-9): 1
   X |   |
  ---+---+---
     |   |
  ---+---+---
     |   |
Thinking...
Calculated 59704 nodes in total
Calculated 7896 winning paths
Shortest path to win is 5 steps
  O @ (0,1) --> XO.......: None
  X @ (0,2) --> XOX......: None
  O @ (1,1) --> XOX.O....: None
  X @ (1,0) --> XOXXO....: None
  O @ (2,1) --> XOXXO..O.: win
Computer plays O at [0,1] as the shortest path to victory
   X | O |
  ---+---+---
     |   |
  ---+---+---
     |   |
Human enter location to play (1-9): 7
   X | O |
  ---+---+---
     |   |
  ---+---+---
   X |   |
Computer plays O at [1,0] to avoid losing
   X | O |
  ---+---+---
   O |   |
  ---+---+---
   X |   |
Human enter location to play (1-9): 6
   X | O |
  ---+---+---
   O |   | X
  ---+---+---
   X |   |
Thinking...
Calculated 60 nodes in total
Calculated 4 winning paths
Shortest path to win is 3 steps
  O @ (1,1) --> XO.OOXX..: None
  X @ (0,2) --> XOXOOXX..: None
  O @ (2,1) --> XOXOOXXO.: win
Computer plays O at [1,1] as the shortest path to victory
   X | O |
  ---+---+---
   O | O | X
  ---+---+---
   X |   |
Human enter location to play (1-9): 9
   X | O |
  ---+---+---
   O | O | X
  ---+---+---
   X |   | X
Argh, detected 2 possible losing locations...
Computer plays O at [0,2] to avoid losing
   X | O | O
  ---+---+---
   O | O | X
  ---+---+---
   X |   | X
Human enter location to play (1-9): 8
   X | O | O
  ---+---+---
   O | O | X
  ---+---+---
   X | X | X
Human won!

```

