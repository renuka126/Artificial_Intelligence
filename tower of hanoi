from collections import deque

def is_legal(state, source, destination):
    # Source peg must not be empty
    if not state[source]:
        return False

    # Destination peg can be empty
    if not state[destination]:
        return True

    # Top disk of source must be smaller than top disk of destination
    return state[source][-1] < state[destination][-1]


def make_move(state, source, destination):
    # Convert state into mutable lists
    new_state = [list(peg) for peg in state]

    # Move top disk
    disk = new_state[source].pop()
    new_state[destination].append(disk)

    # Convert back to tuple so it can be stored in visited
    return tuple(tuple(peg) for peg in new_state)


def display_state(state):
    print(f"A = {list(state[0])}")
    print(f"B = {list(state[1])}")
    print(f"C = {list(state[2])}")


def tower_of_hanoi_bfs(n):
    # Initial state: all disks on peg A
    initial_state = (tuple(range(n, 0, -1)), (), ())

    # Goal state: all disks on peg C
    goal_state = ((), (), tuple(range(n, 0, -1)))

    # Queue for BFS
    queue = deque([initial_state])

    # Visited states
    visited = {initial_state}

    # Parent pointers
    parent = {initial_state: None}

    # Move information
    move_used = {}

    pegs = ['A', 'B', 'C']

    while queue:
        current = queue.popleft()

        # Goal test
        if current == goal_state:
            break

        # Generate all possible source-destination pairs
        for source in range(3):
            for destination in range(3):

                if source == destination:
                    continue

                # Check whether move is legal
                if is_legal(current, source, destination):

                    next_state = make_move(
                        current, source, destination
                    )

                    # Visit only new states
                    if next_state not in visited:
                        visited.add(next_state)
                        parent[next_state] = current

                        disk = current[source][-1]

                        move_used[next_state] = (
                            f"Move disk {disk} from "
                            f"{pegs[source]} to {pegs[destination]}"
                        )

                        queue.append(next_state)

    # Reconstruct solution path
    path = []
    current = goal_state

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    # Display results
    print("\n========== TOWER OF HANOI ==========")
    print("State Space Search using BFS")
    print("====================================")

    print("\nInitial State:")
    display_state(path[0])

    print("\nIntermediate States and Moves:")

    for i in range(1, len(path)):
        print(f"\nStep {i}:")
        print(move_used[path[i]])
        display_state(path[i])

    print("\nFinal State:")
    display_state(path[-1])

    print("\nTotal number of moves:", len(path) - 1)
    print("Total states explored:", len(visited))


# Main program
n = int(input("Enter number of disks: "))

tower_of_hanoi_bfs(n)