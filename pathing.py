import graph_data
import global_game_data
from numpy import random
import heapq
import math
from f_w import get_floyd_warshall_path

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    # global_game_data.graph_paths.append(get_dijkstra_path())
    global_game_data.graph_paths.append(get_floyd_warshall_path())


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
    assert path[0] in graph[0][1]
    assert target_node in path
    assert path[-1] == exit_node
    for i in range(len(path) - 1):
        assert path[i + 1] in graph[path[i]][1]

    return path

def dfs_helper(graph, start_node, target_node):
    stack = [start_node]

    visited = [False] * len(graph)
    visited[start_node] = True

    parents = [0] * len(graph)
    parents[start_node] = -1

    while stack:
        current_node = stack.pop()

        for neighbor in graph[current_node][1]:
            if not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor] = True
                parents[neighbor] = current_node

                # If neighbor is the target then we traverse up the parents to find the path
                if neighbor == target_node:
                    return traverse_parents(parents, neighbor)

def get_dfs_path():
    graph_index = global_game_data.current_graph_index
    graph = graph_data.graph_data[graph_index]

    start_node = 0
    target_node = global_game_data.target_node[graph_index]
    exit_node = len(graph) - 1

    path = dfs_helper(graph, start_node, target_node)

    # Reorient from target to end
    start_node = target_node
    target_node = exit_node

    second_path = dfs_helper(graph, start_node, target_node)

    if (path is not None and second_path is not None):
        path.extend(second_path)

    # Postcondition
    # the path exists
    # the target node is in the path
    # the last node is the exit node
    # each node in the path is connected to the next node
    assert path is not None
    assert target_node in path
    assert path[-1] == exit_node
    for i in range(len(path) - 1):
        assert path[i + 1] in graph[path[i]][1]

    return path


def traverse_parents(parents, current_node):
    path = []
    while parents[current_node] != -1:
        path.insert(0, current_node)
        current_node = parents[current_node]
    return path


def bfs_helper(graph, start_node, target_node):
    current_node = start_node
    queue = [start_node]

    visited = [False] * len(graph)
    visited[start_node] = True

    parents = [0] * len(graph)
    parents[start_node] = -1

    while queue:
        current_node = queue.pop(0)

        for neighbor in graph[current_node][1]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                parents[neighbor] = current_node

                # If neighbor is the target then we traverse up the parents to find the path
                if neighbor == target_node:
                    current_node = neighbor
                    return traverse_parents(parents, current_node)

def get_bfs_path():
    graph_index = global_game_data.current_graph_index
    graph = graph_data.graph_data[graph_index]

    start_node = 0
    target_node = global_game_data.target_node[graph_index]
    exit_node = len(graph) - 1

    path = bfs_helper(graph, start_node, target_node)

    # Reorient from target to end
    start_node = target_node
    target_node = exit_node

    second_path = bfs_helper(graph, start_node, target_node)

    if (path is not None and second_path is not None):
        path.extend(second_path)

    # Postcondition
    # the path exists
    # the target node is in the path
    # the last node is the exit node
    # each node in the path is connected to the next node
    assert path is not None
    assert target_node in path
    assert path[-1] == exit_node
    for i in range(len(path) - 1):
        assert path[i + 1] in graph[path[i]][1]

    return path

def dijkstra_helper(graph, start_node, target_node):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_node))

    distances = [float('inf')] * len(graph)
    distances[start_node] = 0

    parents = [0] * len(graph)
    parents[start_node] = -1

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == target_node:
            return traverse_parents(parents, current_node)

        current_x, current_y = graph[current_node][0]
        for neighbor in graph[current_node][1]:
            neighbor_x, neighbor_y = graph[neighbor][0]
            weight = math.sqrt((current_x - neighbor_x)**2 + (current_y - neighbor_y)**2)
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

def get_dijkstra_path():
    graph_index = global_game_data.current_graph_index
    graph = graph_data.graph_data[graph_index]

    start_node = 0
    target_node = global_game_data.target_node[graph_index]
    exit_node = len(graph) - 1

    path = dijkstra_helper(graph, start_node, target_node)

    # Reorient from target to end
    start_node = target_node
    target_node = exit_node

    second_path = dijkstra_helper(graph, start_node, target_node)

    if path and second_path:
        path.extend(second_path)

    # Postcondition
    # the path exists
    # the path begins at the start node
    # the path ends at the exit node
    # each node in the path is connected to the next node
    assert path
    assert path[0] in graph[0][1]
    assert path[-1] == exit_node
    for i in range(len(path) - 1):
        assert path[i + 1] in graph[path[i]][1]

    return path
