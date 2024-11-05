def is_hamiltonian(graph, path): 
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        if next_node not in graph[current_node][1]:
            return False
    return path[0] in graph[path[-1]][1]

def find_largest_mobile_integer(nodes, directions):
    largest_mobile = -1
    largest_index = -1
    if directions[0] == 1 and nodes[0] > nodes[1]:
        largest_mobile = nodes[0]
        largest_index = 0
    if directions[-1] == -1 and nodes[-1] > nodes[-2] and nodes[-1] > largest_mobile:
        largest_mobile = nodes[-1]
        largest_index = len(nodes) - 1
    for i in range(1, len(nodes)-1):
        if nodes[i] > nodes[i+directions[i]] and nodes[i] > largest_mobile:
            largest_mobile = nodes[i]
            largest_index = i
    return largest_index

def reverse_direction(k, nodes, directions):
    for i in range(len(nodes)):
        if nodes[i] > k:
            directions[i] *= -1

def generate_permutations(nodes):
    directions = [-1] * len(nodes)
    valid_permutations = []
    
    largest_index = find_largest_mobile_integer(nodes, directions)
    valid_permutations.append(nodes[::]) 

    
    while largest_index != -1:

        k = nodes[largest_index] 
        direction = directions[largest_index]
        swap_index = largest_index + direction 

        # Swap k and the adjacent integer it is looking at
        nodes[largest_index], nodes[swap_index] = nodes[swap_index], nodes[largest_index]
        directions[largest_index], directions[swap_index] = directions[swap_index], directions[largest_index]

        reverse_direction(k, nodes, directions)

        largest_index = find_largest_mobile_integer(nodes, directions)
        valid_permutations.append(nodes[::]) 
    
    return valid_permutations

def sjt_hamiltonian_cycles(graph):
    n = len(graph)
    nodes = [i for i in range(1, n-1)]
    valid_cycles = []

    # Generate all permutations
    permutations = generate_permutations(nodes)

    # Check each permutation for Hamiltonian cycle
    for perm in permutations:
        if is_hamiltonian(graph, perm):
            valid_cycles.append(perm)

    if valid_cycles:
        for cycle in valid_cycles:
            print("Hamiltonian Cycle:", cycle)

    return valid_cycles if valid_cycles else -1