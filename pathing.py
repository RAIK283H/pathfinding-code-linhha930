from collections import deque
import heapq
import math
import graph_data
import global_game_data
from numpy import inf, random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    # global_game_data.graph_paths.append(get_test_path())
    # global_game_data.graph_paths.append(get_random_path())
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

    target = global_game_data.target_node[global_game_data.current_graph_index]

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
            next_node = int(random.choice(neighbors))

        path.append(next_node)
        current_node = next_node

        if current_node == end and not target_reached:
            next_node = int(random.choice(neighbors))
            current_node = next_node


    return path 

def get_dfs_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index] 
    start = 0
    end = len(graph) - 1

    target = global_game_data.target_node[global_game_data.current_graph_index]

    path1 = dfs(graph, start, target, visited=[], currpath=[])
    path2 = dfs(graph, target, end, visited=[], currpath=[])
    path = path1 + path2[1:]

    if path is not None:
        assert target in path
        assert path[-1] == end

        for i in range(len(path) - 1):
            assert path[i + 1] in graph[path[i]][1]

    return path


def dfs(graph, node, end, visited, currpath):
    # 'node' here starts out as the start node
    visited.append(node)
    currpath.append(node)

    if node == end:
        return currpath

    for neighbor in graph[node][1]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, end, visited, currpath)
            if path:
                return path

    currpath.pop() 
    return None  


def get_bfs_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index] 
    start = 0
    end = len(graph) - 1

    target = global_game_data.target_node[global_game_data.current_graph_index]

    path1 = bfs(graph, start, target)
    path2 = bfs(graph, target, end)
    path = path1 + path2[1:]

    if path is not None:
        assert target in path
        assert path[-1] == end

        for i in range(len(path) - 1):
            assert path[i + 1] in graph[path[i]][1]

    return path

def bfs(graph, start, end):
    queue = deque([[start]])
    visited = set()  

    while queue:
        path = queue.popleft()  
        node = path[-1]       

        if node == end:
            return path

        if node not in visited: 
            visited.add(node)  

            for neighbor in graph[node][1]: 
                if neighbor not in visited: 
                    new_path = list(path) 
                    new_path.append(neighbor)
                    queue.append(new_path) 

    return None

def get_dijkstra_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    start = 0
    end = len(graph) - 1
    target = global_game_data.target_node[global_game_data.current_graph_index]

    path1 = generate_dijkstra_path(graph, start, target)  
    path2 = generate_dijkstra_path(graph, target, end) 

    full_path = path1 + path2[1:]
    assert target in full_path
    assert full_path[-1] == end

    for i in range(len(full_path) - 1):
            assert full_path[i + 1] in graph[full_path[i]][1]

    return full_path

def generate_dijkstra_path(graph, source, destination):
    dist = [float('inf')] * len(graph) # Store shortest distances
    dist[source] = 0
    parent = [None] * len(graph) # Store parent of each vertex in shortest path tree
    visited = [False] * len(graph) 

    pq = [] # Priority queue
    heapq.heappush(pq, (0, source))

    while pq:
        _, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True

        if u == destination:
            return reconstruct_path(parent, source, destination)
        
        for v in graph[u][1]: 
            alt = dist[u] + dist_between(graph, u, v)
            if not visited[v] and alt < dist[v]: 
                dist[v] = alt
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    return None

def reconstruct_path(parent_arr, source, destination): 
    path = []
    current = destination
    while current is not None: 
        path.append(current)
        current = parent_arr[current]
    path.reverse()
    return path

def dist_between(graph, u, v):
    x1, y1 = graph[u][0]  # Coordinates of node u in graph 
    x2, y2 = graph[v][0]  # Coordinates of node v in graph 
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
