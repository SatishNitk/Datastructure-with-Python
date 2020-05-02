from collections import deque
class AdjGraph:

    def __init__(self):
        self.AdjList = {}

    def add_edge(self, fromvertex, tovertex):
        """ Add the edges , if source does not exists, will add the soucre but not the destination"""
        if fromvertex in self.AdjList.keys():

            self.AdjList[fromvertex].append(tovertex)
        else:
            self.AdjList[fromvertex] = [tovertex]

    def add_vertex(self, vertex):
        if vertex not in self.AdjList.keys():
            self.AdjList[vertex] = []

    def bfs(self, source):
        result = []
        queue = deque()
        visited = [False for _ in range(len(self.AdjList))]
        queue.append(source)
        while len(queue):
            vertex = queue.popleft()
            visited[vertex] = True
            result.append(vertex)
            all_adjacent_of_vertex = self.AdjList[vertex]
            for v in all_adjacent_of_vertex:
                if not visited[v] and v not in queue:
                    queue.append(v)
        print(result)

    def dfs_recursive(self, source, visited, result):
        result.append(source)
        visited[source] = True
        if self.AdjList[source]:
            for v in self.AdjList[source]:
                if not visited[v]:
                    self.dfs_recursive(v, visited, result)
    
    def dfs_recursive_call(self, source):
        result = []
        visited = [False for _ in range(len(self.AdjList))]
        self.dfs_recursive(source, visited, result)
        print("recursive dfs result:-",result)


    def check_for_cycle(self, source, visited, rec_stack):
        visited[source] = True
        rec_stack.append(source)
        if self.AdjList[source]:
            for v in self.AdjList[source]:
                if not visited[v] and self.check_for_cycle(v, visited, rec_stack):
                        return True
                elif visited[v]:
                    return True
        visited[source] = False
        return False


    def iscycle(self):
        visited = [False for _ in range(len(self.AdjList))]
        rec_stack = deque()
        count = 0
        for source in self.AdjList.keys():
            if self.check_for_cycle(source, visited, rec_stack):
                return True
        return False


    def dfs(self, source):
        result = []
        stack = deque()
        visited = [False for _ in range(len(self.AdjList))]
        stack.append(source)
        result.append(source)
        visited[source] = True
        while  len(stack):
            flag = False
            vertex = stack[-1]
            if self.AdjList[vertex]:
                for v in self.AdjList[vertex]:
                    if not visited[v]:
                        flag  = True
                        visited[v] = True
                        stack.append(v)
                        result.append(v)
                        break
                if not flag:
                    print("sa")
                    stack.pop()
            else:
                stack.pop()
        print(result)


    def display(self):
        for edge in self.AdjList:
            print(str(edge) + "->" + "->".join(str(e) for e in self.AdjList[edge]))


if __name__ == "__main__":
    obj = AdjGraph()
    obj.add_vertex(0)
    obj.add_vertex(1)
    obj.add_vertex(2)
    obj.add_vertex(3)


    obj.add_edge(0,1)
    obj.add_edge(1,2)
    obj.add_edge(2,3)
    obj.add_edge(2,0)
    obj.add_edge(0,2)
    obj.add_edge(3,3)



    obj.display()
    # obj.bfs(0)
    obj.dfs(2)
    # obj.dfs_recursive_call(0)
    # print("cycle present status ",obj.iscycle())