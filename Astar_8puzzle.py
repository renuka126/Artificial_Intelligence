import heapq

# Goal state
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Display the puzzle
def display_state(state):
    print("+---+---+---+")
    for i in range(0, 9, 3):
        print("|", end=" ")
        for j in range(i, i + 3):
            if state[j] == 0:
                print(" ", end=" | ")
            else:
                print(state[j], end=" | ")
        print()
        print("+---+---+---+")


# Calculate Manhattan distance h(n)
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            current_row = i // 3
            current_col = i % 3

            goal_index = GOAL.index(state[i])
            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


# Generate all possible successor states
def get_neighbors(state):
    neighbors = []

    blank_position = state.index(0)

    row = blank_position // 3
    col = blank_position % 3

    moves = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dr, dc, move in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_position = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with tile
            new_state[blank_position], new_state[new_position] = \
                new_state[new_position], new_state[blank_position]

            neighbors.append((tuple(new_state), move))

    return neighbors


# A* Search
def a_star(start):

    # Priority queue
    open_list = []

    h = heuristic(start)

    # (f, g, state)
    heapq.heappush(open_list, (h, 0, start))

    # Store the best cost
    g_cost = {start: 0}

    # Parent information
    parent = {start: None}

    # Move information
    move_used = {}

    while open_list:

        f, g, current = heapq.heappop(open_list)

        # Goal test
        if current == GOAL:
            break

        # Generate successors
        for neighbor, move in get_neighbors(current):

            new_g = g + 1

            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                g_cost[neighbor] = new_g

                h = heuristic(neighbor)
                new_f = new_g + h

                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor)
                )

                parent[neighbor] = current
                move_used[neighbor] = move

    # Reconstruct path
    path = []
    current = GOAL

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, g_cost


# Main program
print("========== 8 PUZZLE USING A* ==========")

# This example requires 6 moves to solve
initial_state = (
    1, 2, 3,
    4, 5, 6,
    0, 7, 8
)

print("\nInitial State:")
display_state(initial_state)

print("\nGoal State:")
display_state(GOAL)

# Run A*
path, g_cost = a_star(initial_state)

print("\n========== A* SOLUTION ==========")

# Display initial state
print("\nInitial State")
display_state(path[0])

h = heuristic(path[0])
g = 0
f = g + h

print("g(n) =", g)
print("h(n) =", h)
print("f(n) = g(n) + h(n)")
print("f(n) =", f)

# Display intermediate states
for i in range(1, len(path)):

    state = path[i]

    g = i
    h = heuristic(state)
    f = g + h

    print("\n--------------------------------")
    print("Step", i)
    print("--------------------------------")

    display_state(state)

    print("g(n) =", g)
    print("h(n) =", h)
    print("f(n) = g(n) + h(n)")
    print("f(n) =", g, "+", h, "=", f)

# Final result
print("\n========== FINAL RESULT ==========")
print("Goal State Reached!")

display_state(GOAL)

print("Total moves =", len(path) - 1)