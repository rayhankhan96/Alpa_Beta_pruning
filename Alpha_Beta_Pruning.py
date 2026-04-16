import random

def generate_leaves(n):
    return [random.randint(1, 20) for _ in range(n)]

def minimax(depth, index, is_max, leaves, height, count):
    count[0] += 1
    if depth == height:
        return leaves[index]
    if is_max:
        return max(
            minimax(depth+1, index*2, False, leaves, height, count),
            minimax(depth+1, index*2+1, False, leaves, height, count)
        )
    else:
        return min(
            minimax(depth+1, index*2, True, leaves, height, count),
            minimax(depth+1, index*2+1, True, leaves, height, count)
        )

def alphabeta(depth, index, is_max, leaves, height, alpha, beta, count, pruned):
    count[0] += 1
    if depth == height:
        return leaves[index]
    if is_max:
        value = -float('inf')
        for i in range(2):
            value = max(value, alphabeta(depth+1, index*2+i, False, leaves, height, alpha, beta, count, pruned))
            alpha = max(alpha, value)
            if beta <= alpha:
                pruned[0] += 1
                break
        return value
    else:
        value = float('inf')
        for i in range(2):
            value = min(value, alphabeta(depth+1, index*2+i, True, leaves, height, alpha, beta, count, pruned))
            beta = min(beta, value)
            if beta <= alpha:
                pruned[0] += 1
                break
        return value

leaf_count = 8
leaves = generate_leaves(leaf_count)

height = 3

minimax_count = [0]
optimal_value = minimax(0, 0, True, leaves, height, minimax_count)

ab_count = [0]
pruned = [0]
ab_value = alphabeta(0, 0, True, leaves, height, -float('inf'), float('inf'), ab_count, pruned)

efficiency = ((minimax_count[0] - ab_count[0]) / minimax_count[0]) * 100

print("Generated Leaf Nodes:", leaves)

print("\nMinimax:")
print("Nodes Evaluated:", minimax_count[0])
print("Optimal Value:", optimal_value)

print("\nAlpha-Beta Pruning:")
print("Nodes Evaluated:", ab_count[0])
print("Nodes Pruned:", pruned[0])

print(f"\nEfficiency Improvement: {efficiency:.2f}%")