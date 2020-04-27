class AdjacencyListGraph:

    def __init__(self):
        self.AdjList= {}

    def add_edge(self, fromvertex, tovertex):
        if fromvertex  in self.AdjList.keys():
            self.AdjList[fromvertex].append(tovertex)
        else:
            self.AdjList[fromvertex] = [tovertex]

    def remove_edge(self, fromvertex, tovertex):
        if fromvertex in self.AdjList.keys() and tovertex in self.AdjList.keys():
            self.AdjList[fromvertex].remove(tovertex)
        else:
            print("source and destination does not exists")

    def delete_vertex(self, vertex):
        if vertex in self.AdjList.keys():
            del self.AdjList[vertex]
        else:
            print("vertex does not exists")

    def add_vertex(self, vertex):
        if vertex not in self.AdjList.keys():
            self.AdjList[vertex] = []
        else:
            print("vertex already exists")

    def display(self):

        for edge in self.AdjList:
            print(str(edge)+ "->"  + "->".join([str(j) for j in  self.AdjList[edge]]))

if __name__ == '__main__':

    adj = AdjacencyListGraph()
    adj.add_edge(0, 1)
    adj.add_edge(0, 4)
    adj.add_edge(4, 1)
    adj.add_edge(4, 3)
    adj.add_edge(1, 0)
    adj.add_edge(1, 4)
    adj.add_edge(1, 3)
    adj.add_edge(1, 2)
    adj.add_edge(2, 3)
    adj.add_edge(3, 4)
    adj.display()
    adj.remove_edge(3,4)
    adj.remove_edge(33,4)
    print("after removing edged")
    adj.display()
    print("after vertex delete")
    adj.delete_vertex(3)
    adj.delete_vertex(1)
    adj.display()
    print("After adding vertex")
    adj.add_vertex(3)
    adj.add_vertex(1)
    adj.display()


