# SearchAlgVisual
Interactive program to visually demonstrate various search algorithms including A*, Djikstra’s, and BFS. 

Right clicking on an empty node will create a start point. Right clicking on another empty node will create and endpoint (if a start point does not exist). Left clicking on an empty node will generate an obstruction, or a node in which the search algorithm may not go through. Right clicking on any non-empty node will reset the node to its empty default.

A weight button is available to observe the behavior of weight-sensitive search algorithms such as Djikstra's. All nodes are initialized with a weight of 1. Clicking on the weight button will increase the weight, from 1 up to 5. With a weight selected, hover over any node and press the 'w' key to apply the weight to the selected node. Applying a weight of 1 to a node will reset that node to its default weight.

Clicking on any button labeled with a search algorithm will begin an attempt to solve the given board state using the selected search algorithm.

Clicking on the button labeled reset will refresh the board.

## main.py
Main function. Calls on GUI helper file and handles high-level actions such as clearing and search algorithm selection

## algorithms
Directory to hold search algorithm functions

## helpers
Directory to hold back-end modules

### graph.py
Contains graph data structure and graph initializer functions

### node.py
Contains node class and node member functions

### searchgui.py
Handles graphics and user interface
