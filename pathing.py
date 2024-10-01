import graph_data
import global_game_data
from numpy import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    graph_index = global_game_data.current_graph_index
    graph = graph_data.graph_data[graph_index]

    start_node = 0
    target_node = global_game_data.target_node[graph_index]
    exit_node = len(graph) - 1

    # Precondition
    # Ensure that there is a start node, a target node, and an exit node to target
    assert graph[start_node]
    assert graph[target_node]
    assert graph[exit_node]

    path = []
    current_node = start_node

    while current_node != target_node:
        neighbors = graph[current_node][1]
        neighbors_count = len(neighbors)

        random_index = int(random.randint(neighbors_count))
        random_neighbor = neighbors[random_index]

        current_node = random_neighbor
        path.append(current_node)

        # If we reach the target node, we need to change the target to the exit node
        if current_node == target_node:
            target_node = exit_node

    # Postcondition
    # Ensure in path that the first node is connected to the start node
    # the target node is in the path
    # the last node is the exit node
    # each node in the path is connected to the next node
    assert start_node in graph[path[0]][1]
    assert target_node in path
    assert path[-1] == exit_node
    for i in range(len(path) - 1):
        assert path[i + 1] in graph[path[i]][1]

    return path

def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
