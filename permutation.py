"""
This module implements the Steinhaus-Johnson-Trotter algorithm for generating permutations.
"""


def get_permutations_sjt(n):
    """
    Generates all permutations of numbers from 1 to n-1 using Steinhaus-Johnson-Trotter.

    Args:
        n (int): The upper limit (exclusive) for generating permutations.

    Returns:
        list: A list of all permutations.
    """

    def get_largest_mobile(permutation, directions):
        largest_mobile_integer = -1
        largest_mobile_index = -1
        for mobile_index, mobile_integer in enumerate(permutation):
            if mobile_integer > largest_mobile_integer:
                direction = directions[mobile_index]
                adjacent_index = mobile_index + direction
                if adjacent_index > -1 and adjacent_index < len(permutation):
                    adjacent_integer = permutation[adjacent_index]

                    if mobile_integer > adjacent_integer:
                        largest_mobile_integer = mobile_integer
                        largest_mobile_index = mobile_index

        return (largest_mobile_index, largest_mobile_integer)

    all_permutations = []
    permutation = list(range(1, n))
    all_permutations.append(permutation.copy())

    # -1 means left (thus index - 1 = number to the left)
    # 1 means right (thus index + 1 = number to the right)
    directions = [-1] * (n - 1)

    mobile = True

    while mobile:
        # Get largest_mobile and then adjacent variables
        largest_mobile_index, largest_mobile_integer = get_largest_mobile(
            permutation, directions
        )
        if largest_mobile_index == -1:
            mobile = False
            continue

        largest_mobile_direction = directions[largest_mobile_index]

        adjacent_index = largest_mobile_index + largest_mobile_direction
        adjacent_integer = permutation[adjacent_index]
        adjacent_direction = directions[adjacent_index]

        # Do the swap of values and then direction
        permutation[largest_mobile_index] = adjacent_integer
        permutation[adjacent_index] = largest_mobile_integer

        directions[largest_mobile_index] = adjacent_direction
        directions[adjacent_index] = largest_mobile_direction

        # Reverse direction of all integers larger than k
        for i, _ in enumerate(directions):
            if permutation[i] > largest_mobile_integer:
                directions[i] *= -1

        all_permutations.append(permutation.copy())

    return all_permutations


def get_hamiltonian_cycles(graph):
    """
    Takes in a graph, calls sjt to generate permutations, and then responds with hamiltonian cycles.

    Args:
        graph (graph_data[i]): The graph to inspect

    Returns:
        list: list of all hamiltonian cycles
    """
    graph_length = len(graph)
    permutations = get_permutations_sjt(graph_length - 1)
    hamiltonian_cycles = []

    for permutation in permutations:
        is_hamiltonian_cycle = True
        for i, node in enumerate(permutation):
            next_node = None
            # If over loop back to start
            if i + 1 >= len(permutation):
                next_node = permutation[0]
            else:
                next_node = permutation[i + 1]
            
            current_node_connections = graph[node][1]

            if next_node not in current_node_connections:
                is_hamiltonian_cycle = False
                break
        if is_hamiltonian_cycle:
            hamiltonian_cycles.append(permutation)

    if len(hamiltonian_cycles) == 0:
        return -1

    return hamiltonian_cycles
