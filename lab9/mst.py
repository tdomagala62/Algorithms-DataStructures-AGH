import graf_mst


class Vertex:
    def __init__(self, key, color=None):
        self.key = key
        self.color = color

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __repr__(self):
        return self.key


class Edge:
    def __init__(self, cost):
        self.cost = cost

    def __repr__(self):
        return str(self.cost)


class ListOfNeighbours:
    def __init__(self):
        self.list = []          # list of dictionaries - [{1st vertex.key : Edge}, {2nd vertex.key : Edge}, ...]
        self.vertex_list = []   # list of vertex objects
        self.dict = {}          # vertex key ---> vertex index in list

    def isEmpty(self):
        return len(self.list) == 0

    def insertVertex(self, vertex: Vertex):
        if vertex not in self.vertex_list:
            self.list.append({})
            self.vertex_list.append(vertex)
            self.dict[vertex.key] = self.order() - 1

    def insertEdge(self, vertex1: Vertex, vertex2: Vertex, edge=Edge(0)):
        if vertex1 not in self.vertex_list:
            self.insertVertex(vertex1)
        if vertex2 not in self.vertex_list:
            self.insertVertex(vertex2)

        self.list[self.getVertexIdx(vertex1)][vertex2.key] = edge

    def deleteVertex(self, vertex: Vertex):
        if vertex in self.vertex_list:
            vertex_idx = self.getVertexIdx(vertex)
            self.list.pop(vertex_idx)
            for dictionary in self.list:
                dictionary.pop(vertex.key, None)
            self.dict.pop(vertex.key)
            for idx in range(vertex_idx + 1, self.order()):
                self.dict[self.vertex_list[idx]] = idx - 1
            self.vertex_list.pop(vertex_idx)

    def deleteEdge(self, vertex1: Vertex, vertex2: Vertex):
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list:
            self.list[self.getVertexIdx(vertex1)].pop(vertex2.key)

    def getVertexIdx(self, vertex: Vertex):
        return self.dict[vertex.key]

    def getVertex(self, vertex_idx) -> Vertex:
        return self.vertex_list[vertex_idx]

    def neighboursIdx(self, vertex_idx):
        return [self.getVertexIdx(self.vertex_list[self.dict[key]]) for key in self.list[vertex_idx].keys()]

    def order(self):
        return len(self.vertex_list)

    def size(self):
        result = 0
        for dictionary in self.list:
            result += len(dictionary)
        return result

    def edges(self):
        result = []
        for idx, dictionary in enumerate(self.list):
            vertex1 = self.getVertex(idx)
            result += [(vertex1.key, vertex2) for vertex2 in dictionary.keys()]
        return result

    def display(self):
        print("--------------------")
        for idx, dictionary in enumerate(self.list):
            vertex1 = self.getVertex(idx)
            print(vertex1.key, "-", dictionary)
        print("--------------------")


def MST(G: ListOfNeighbours):
    size = G.order()
    intree = size*[0]
    distance = size*[float('inf')]
    parent = size*[-1]
    tree = ListOfNeighbours()

    for vertex in G.vertex_list:
        tree.insertVertex(vertex)
    current_vertex_idx = 0
    length_of_tree = 0

    while intree[current_vertex_idx] == 0:
        intree[current_vertex_idx] = 1
        for vertex_idx in G.neighboursIdx(current_vertex_idx):
            if intree[vertex_idx] == 0 and G.list[current_vertex_idx][G.vertex_list[vertex_idx].key].cost < distance[vertex_idx]:
                distance[vertex_idx] = G.list[current_vertex_idx][G.vertex_list[vertex_idx].key].cost
                parent[vertex_idx] = current_vertex_idx

        min_distance = (-1, float('inf'))   # tuple (vertex_idx, min_distance_value)
        for vertex_idx in range(G.order()):
            if intree[vertex_idx] == 0:
                if distance[vertex_idx] < min_distance[1]:
                    min_distance = vertex_idx, distance[vertex_idx]

        edge = G.list[parent[min_distance[0]]][G.vertex_list[min_distance[0]].key]
        if min_distance[0] >= 0:
            length_of_tree += edge.cost
        tree.insertEdge(G.vertex_list[parent[min_distance[0]]], G.vertex_list[min_distance[0]], edge)
        tree.insertEdge(G.vertex_list[min_distance[0]], G.vertex_list[parent[min_distance[0]]], edge)

        current_vertex_idx = min_distance[0]
    return tree, length_of_tree


def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighboursIdx(i)
        for idx in nbrs:
            print(g.getVertex(idx), g.list[i][g.vertex_list[idx].key], end=";")
        print()
    print("-------------------")


if __name__ == "__main__":
    graph = ListOfNeighbours()
    for i in graf_mst.graf:
        graph.insertEdge(Vertex(i[0]), Vertex(i[1]), Edge(i[2]))
        graph.insertEdge(Vertex(i[1]), Vertex(i[0]), Edge(i[2]))
    tree, length_of_tree = MST(graph)
    printGraph(tree)
