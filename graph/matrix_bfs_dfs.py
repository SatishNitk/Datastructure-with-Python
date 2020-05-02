from collections import deque
class Graph:

    def __init__(self, n):
        self.n = n
        self.mat  = [[0 for _ in range(n)] for _ in range(n)]


    def add_edge(self, fromvertex, tovertex):
        if fromvertex >= self.n or tovertex >= self.n:
            print("Source  and Destination does not exists")
            return
        else:
            self.mat[fromvertex][tovertex] = 1
            # self.mat[tovertex][fromvertex] = 1

    def remove_edge(self, fromvertex, tovertex):
        if fromvertex >= self.n or tovertex >= self.n:
            print("Source  and Destination does not exists")
            return
        else:
            self.mat[fromvertex][tovertex] = 0
            # self.mat[tovertex][fromvertex] = 0

    def add_vertex(self):
        self.n = self.n + 1
        
        self.mat.append([0 for _ in range(self.n-1)])

        for i in range(self.n):
            self.mat[i][self.n-1] = 0

    def display_graph(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.mat[i][j], end = "")
            print()

    def dfs(self, source):
        stack = deque()
        visited = [False for _ in range(self.n)]
        result = []
        result.append(source)
        visited[source] = True
        stack.append(source)
        while  stack:
            flag = True
            source = stack[-1]
            for i in range(self.n):
                if  self.mat[source][i] and not visited[i]:
                    stack.append(i)
                    result.append(i)
                    visited[i] = True
                    flag = False
                    break
            if flag:
                stack.pop()

        print(result)

    def connected_componenet(self):
        visited = [False for _ in range(len(self.mat[0]))]
        counter = 0
        for v in range(len(self.mat[0])):
            if not visited[v]:
                counter += 1 
                self.dfs_recursive(v, visited)
        print("Number of connected_componenet", counter)

    def dfs_recursive(self, source, visited):
        visited[source] = True
        print(source)
        for i in range(self.n):
            if self.mat[source][i] and not visited[i]:
                self.dfs_recursive(i, visited)




graph = Graph(4)
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,2)
graph.add_edge(2,3)
graph.add_edge(2,0)
graph.add_edge(3,3)


graph.display_graph()
graph.dfs(0)
graph.dfs_recursive(0, [False for _ in range(4)])
graph.connected_componenet()