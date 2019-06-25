# Cops-and-Robbers
Game Implementation in Python.
Two players, a cop (C), and a robber (R), compete on a fixed, finite undirected graph H. 

First, the cop starts by placing himself at a node of his choice; then the robber does the same. After that, the two players alternate (beginning with the cop) moving to an adjacent node or choosing not to move. All moves are seen by both players. (Here we modified the original rules of Winkler by allowing the robber "not to move".) 

The cop wins the game if he can CAPTURE the robber, that is, 
move onto the node that is occupied by the robber or the robber (is forced to) move onto the node that is occupied by the cop .
The robbers wins if he is able to avoid being captured indefinitely. 
