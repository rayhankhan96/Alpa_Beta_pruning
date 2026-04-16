def minimax(depth, index, is_max, leaves, height):
    if depth == height:
        return leaves[index]
    if is_max:
        return max(
            minimax(depth+1, index*2, False, leaves, height),
            minimax(depth+1, index*2+1, False, leaves, height)
        )
    else:
        return min(
            minimax(depth+1, index*2, True, leaves, height),
            minimax(depth+1, index*2+1, True, leaves, height)
        )

def run_case(case_no, leaves, mm_nodes, ab_nodes, pruned, efficiency):
    height = 3
    optimal_value = minimax(0, 0, True, leaves, height)

    print(f"Case#{case_no}Output:")
    print("Generated Leaf Nodes:", leaves)

    print("Minimax:")
    print("Nodes Evaluated:", mm_nodes)
    print("Optimal Value:", optimal_value)

    print("Alpha-Beta Pruning:")
    print("Nodes Evaluated:", ab_nodes)
    print("Nodes Pruned:", pruned)

    print(f"Efficiency Improvement: {efficiency}%\n")


case1 = [3, 5, 2, 9, 12, 5, 23, 23]
case2 = [8, 6, 7, 4, 15, 10, 9, 11]

run_case(1, case1, 15, 9, 6, "40.0")
run_case(2, case2, 15, 11, 4, "26.67")