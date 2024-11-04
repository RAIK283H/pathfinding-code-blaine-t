import graph_data
import permutation

if __name__ == "__main__":
    graph = graph_data.graph_data[4]
    hamiltonian_cycles = permutation.get_hamiltonian_cycles(graph)
    print(hamiltonian_cycles)
