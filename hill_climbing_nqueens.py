

import random

def calculate_conflicts(board):
    """Count pairs of queens attacking each other"""
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Same row or same diagonal (columns are already unique by construction)
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_neighbors(board):
    """Generate all boards differing by moving one queen within its column"""
    n = len(board)
    neighbors = []
    for col in range(n):
        for row in range(n):
            if row != board[col]:
                new_board = board[:]
                new_board[col] = row
                neighbors.append(new_board)
    return neighbors

def hill_climbing(n):
    # Random initial state: one queen per column, random row
    current = [random.randint(0, n - 1) for _ in range(n)]
    current_cost = calculate_conflicts(current)

    steps = 0
    while True:
        steps += 1
        neighbors = get_neighbors(current)
        neighbor_costs = [(nb, calculate_conflicts(nb)) for nb in neighbors]
        best_neighbor, best_cost = min(neighbor_costs, key=lambda x: x[1])

        if best_cost >= current_cost:
            # No better neighbor -> stuck at local optimum (or solved)
            break

        current, current_cost = best_neighbor, best_cost

    return current, current_cost, steps

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            line += " Q " if board[col] == row else " . "
        print(line)
    print()

def solve_with_restarts(n, max_restarts=100):
    for attempt in range(1, max_restarts + 1):
        solution, cost, steps = hill_climbing(n)
        if cost == 0:
            print(f"Solved on attempt {attempt} (in {steps} steps):\n")
            print_board(solution)
            return solution
    print("No solution found within restart limit.")
    return None

if __name__ == "__main__":
    n = int(input("Enter number of queens (N): "))
    solve_with_restarts(n)