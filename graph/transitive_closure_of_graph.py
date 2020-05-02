from collections import defaultdict, deque
class Graph:

    def __init__(self, n):
        self.n = n
        self.graph = defaultdict()

    def add_edge(self, fromvertex, tovertex):
        if fromvertex  in self.graph.keys():
            self.graph[fromvertex].append(tovertex)
        else:
            self.graph[fromvertex] = [tovertex]

    def display(self):
        for key, value in self.graph.items():
            print(str(key) + "->" + "->".join(str(v) for v in value))

    def dfsUtil(self, source, graph, visited, result) -> list:
        visited[source] = True
        result[source] = 1

        for v in graph[source]:
            if not visited[v]:
                self.dfsUtil(v, graph, visited, result)
        return result


    def transitive_closure_of_graph(self):
        result = []
        for source in range(self.n):
            data = [0 for _ in range(self.n)]
            visited = [False for _ in range(self.n)]
            data = self.dfsUtil(source, self.graph, visited, data)
            result.append(data)
        print("Transitive Closure of graph :-", result)



graph = Graph(4)
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,2)
graph.add_edge(2,0)
graph.add_edge(2,3)
graph.add_edge(3,3)
graph.display()
graph.transitive_closure_of_graph()