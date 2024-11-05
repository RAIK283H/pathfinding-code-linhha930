from graph_data import graph_data
from permutation import sjt_hamiltonian_cycles

# sjt_hamiltonian_cycles(graph_data[1])

graph_index = 1
print("Graph Data:")
for i, (coords, neighbors) in enumerate(graph_data[graph_index]):
    print(f"Node {i}: Coordinates {coords}, Neighbors {neighbors}")

sjt_hamiltonian_cycles(graph_data[graph_index])