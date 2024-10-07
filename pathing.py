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
    graph = graph_data.graph_data[global_game_data.current_graph_index] 
    # Precondition: a valid graph exists
    assert graph is not None
    start = 0
    end = len(graph) - 1 

    potential_targets = [i for i in range(len(graph)) if i != start and i != end]
    target = random.choice(potential_targets)

    path = generate_random_path(graph, start, end, target)
    # Postcondition: cannot return an empty path
    assert start in path
    assert end in path
    assert path

    return path

def generate_random_path(graph, start, end, target): 
    path = [start]
    current_node = start 
    target_reached = False

    while current_node != end or not target_reached:
        neighbors = graph[current_node][1]

        if not target_reached and target in neighbors:
            next_node = target
            target_reached = True
        else:
            next_node = random.choice(neighbors)

        path.append(next_node)
        current_node = next_node

        if current_node == end and not target_reached:
            next_node = random.choice(neighbors)
            current_node = next_node


    return path 


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
