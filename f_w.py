import global_game_data
import graph_data
import math


def adjacency_list_to_matrix(index):
    adjacency_list = graph_data.graph_data[index]
    adjacency_list_size = len(adjacency_list)
    matrix = [[float('inf')] * adjacency_list_size for i in range(adjacency_list_size)]
    for i in range(adjacency_list_size):
        matrix[i][i] = 0
    for i, entry in enumerate(adjacency_list):
        neighbor = adjacency_list[i]
        neighbor_x = neighbor[0][0]
        neighbor_y = neighbor[0][1]
        for num in entry[1]:
            current = adjacency_list[num]
            current_x = current[0][0]
            current_y = current[0][1]
            matrix[i][num] = math.sqrt((current_x - neighbor_x)**2 + (current_y - neighbor_y)**2)
    return matrix

def floyd_warshall(W):
    matrix_length = len(W)
    P = [[None] * matrix_length for i in range(matrix_length)]
    for k in range(matrix_length):
        for i in range(matrix_length):
            for j in range(matrix_length):
                if W[i][k] < float('inf') and W[k][j] < float('inf') and W[i][k] + W[k][j] < W[i][j]:
                    W[i][j] = W[i][k] + W[k][j]
                    P[i][j] = k
    return P

def floyd_warshall_path(P, i, j):
    # Why does recursion work better than iteration AHHHH
    if P[i][j] is None:
        return [i, j]
    path = floyd_warshall_path(P, i, P[i][j])
    path.pop()
    path.extend(floyd_warshall_path(P, P[i][j], j))
    return path

def get_floyd_warshall_path(index):
    matrix = adjacency_list_to_matrix(index)
    start = 0
    target = 3
    end = len(matrix) - 1
    P = floyd_warshall(matrix)
    startToTarget = floyd_warshall_path(P, start, target)
    targetToEnd = floyd_warshall_path(P, target, end)
    startToTarget.pop(0)
    startToTarget.pop()
    startToTarget.extend(targetToEnd)
    return startToTarget

print(get_floyd_warshall_path(4))
