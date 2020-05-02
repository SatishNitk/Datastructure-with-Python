from collections import deque


def is_safe(graph, i, j, n, visited):

    if i <0 or i>=n or j<0 or j>= n:
        return False
    if not visited[i][j] and graph[i][j]:
        return True

def dfsutil(graph, i, j,  n, visited):

    visited[i][j] = True

    row = [-1, -1, -1, 0, 0, 1, 1, 1]
    col = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(8):
        if is_safe(graph, i, j, n, visited):
            dfsutil(graph, i, j, n, visited)

def number_of_island(graph, n):
    visited = [[False for _ in range(n)] for _ in range(n)]
    counter = 0
    for i in range(5):
        for j in range(5):
            if not visited[i][j] and graph[i][j]:
                counter += 1
                dfsutil(graph,i,j, n, visited)

    print("NUmber of island : -", counter)

if __name__ == '__main__':
    graph = [[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 1]] 
    number_of_island(graph, 5)
