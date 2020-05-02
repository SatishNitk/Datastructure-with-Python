from collections import defaultdict, deque
class Graph:
    def __init__(self, n):
        self.n = n 
        self.graph = defaultdict()
    
    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]


    def display(self):
        for key, value in self.graph.items():
            print(str(key) + "->" + "->".join([str(i) for i in value]))

    def dfsUtil(self, graph, source, destination, visited):
        stack = deque()
        visited[source] = True
        result = []
        result.append(source)
        stack.append(source)
        while stack:
            v = stack[-1]
            flag = True
            for k in self.graph[v]:
                if not visited[k]:
                    if k == destination:
                        stack.append(destination)
                        result = stack.copy()
                        stack.clear()
                    else:
                        stack.append(k)
                        visited[k] = True
                        result.append(k)
                    flag = False
                    break
            if  flag:
                stack.pop()
        return result

    def path(self, source, destination):
        visited = [False for _ in range(self.n)]
        print(self.dfsUtil(self.graph, source, destination, visited))

graph = Graph(6)
graph.add_edge(1,0)
graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,1)
graph.add_edge(1,5)
graph.add_edge(5,1)
graph.add_edge(3,5)
graph.add_edge(5,3)
graph.add_edge(5,4)
graph.add_edge(4,5)

graph.display()
graph.path(0,4)



