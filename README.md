# Alpa_Beta_pruning

You are required to implement a Python program that generates a random binary game tree with leaf node scores (for example, 8 or 16 leaf nodes). The program must apply both the Minimax algorithm and the Alpha-Beta Pruning algorithm on the same tree to determine the optimal value. It should also count and display how many nodes are evaluated in each algorithm, how many nodes are pruned in Alpha-Beta Pruning, and finally calculate the percentage improvement in efficiency achieved by Alpha-Beta Pruning compared to Minimax. No input is required, as the leaf node values will be generated randomly within the program.

Case#1Output:
Generated Leaf Nodes: [3, 5, 2, 9, 12, 5, 23, 23]
Minimax:
    Nodes Evaluated: 15
    Optimal Value: 12
Alpha-Beta Pruning:
    Nodes Evaluated: 9
    Nodes Pruned: 6
Efficiency Improvement: 40.0%

Case#2Output:
Generated Leaf Nodes: [8, 6, 7, 4, 15, 10, 9, 11]
Minimax:
    Nodes Evaluated: 15
    Optimal Value: 9
Alpha-Beta Pruning:
    Nodes Evaluated: 11
    Nodes Pruned: 4
Efficiency Improvement: 26.67%
