import graph_data


def adjacency_list_to_matrix(index):
    adjacency_list = graph_data.graph_data[index]
    adjacency_list_size = len(adjacency_list)
    matrix = [[0] * adjacency_list_size for i in range(adjacency_list_size)]
    for i, entry in enumerate(adjacency_list):
        for num in entry:
            matrix[i][num] = 1
    return matrix