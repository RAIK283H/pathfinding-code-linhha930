import math
import graph_data


def floyd_warshall(graph):
    distance = adj_list_to_matrix(graph)
    parent = [[0] * len(graph) for i in range (len(graph))]

    for k in range(len(graph)): 
        for i in range (len(graph)):
            for j in range (len(graph)): 
                if distance[i][k] + distance[k][j] < distance[i][j]: 
                    distance[i][j] = distance[i][k] + distance[k][j]
                    parent[i][j] = k
    
    return distance, parent


def adj_list_to_matrix(graph): 
    matrix = [[float('inf')] * len(graph) for _ in range(len(graph))]

    for i in range(len(graph)): 
        for j in range(len(graph)): 
            for j in graph[i][1]: 
                matrix[i][j] = math.sqrt((graph[i][0][0] - graph[j][0][0]) ** 2 + (graph[i][0][1] - graph[j][0][1]) ** 2)
                
    return matrix

def build_path(parent_matrix, start, end): 
    path = []
    current = end

    while current != start: 
        if current == -1: # Check for invalid parent
            return []
        path.append(current)
        current = parent_matrix[start][current]
        
    path.append(start)
    return path[::-1]
