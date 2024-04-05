import polska


class Vertex:
    def __init__(self, key):
        self.key = key

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


class MatrixOfNeighbours:
    def __init__(self):
        self.matrix = []
        self.vertex_list = []  # List of vertex's key
        self.dict = {}         # vertex key ---> vertex index in list

    def isEmpty(self):
        return len(self.matrix) == 0

    def insertVertex(self, vertex):
        if vertex not in self.vertex_list:
            self.vertex_list.append(vertex)
            self.dict[vertex] = self.order() - 1
            if self.isEmpty():
                self.matrix.append([None])
            else:
                for row in self.matrix:
                    row.append(None)
                self.matrix.append([None for i in range(self.order())])

    def insertEdge(self, vertex1, vertex2, edge=Edge(0)):
        if vertex1 not in self.vertex_list:
            self.insertVertex(vertex1)
        if vertex2 not in self.vertex_list:
            self.insertVertex(vertex2)

        self.matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = edge

    def deleteVertex(self, vertex):
        if vertex in self.vertex_list:
            vertex_idx = self.getVertexIdx(vertex)
            self.matrix.pop(vertex_idx)
            for row in self.matrix:
                row.pop(vertex_idx)
            self.dict.pop(vertex)
            for idx in range(vertex_idx + 1, self.order()):
                self.dict[self.vertex_list[idx]] = idx - 1
            self.vertex_list.pop(vertex_idx)

    def deleteEdge(self, vertex1, vertex2):
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list:
            self.matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = None

    def getVertexIdx(self, vertex):
        return self.dict[vertex]

    def getVertex(self, vertex_idx):
        return self.vertex_list[vertex_idx]

    def neighboursIdx(self, vertex_idx):
        return [idx for idx, edge in enumerate(self.matrix[vertex_idx]) if edge]

    def order(self):
        return len(self.vertex_list)

    def size(self):
        result = 0
        for row in self.matrix:
            for edge in row:
                if edge:
                    result += edge.cost
        return result

    def edges(self):
        result = []
        for i in range(self.order()):
            for j in range(self.order()):
                if self.matrix[i][j]:
                    result.append((self.getVertex(i), self.getVertex(j)))
        return result

    def display(self):
        print("--------------------")
        for row in self.matrix:
            print(row)
        print("--------------------")


class ListOfNeighbours:
    def __init__(self):
        self.list = []          # list of dictionaries - {vertex : edge}
        self.vertex_list = []   # list of vertex's key
        self.dict = {}          # vertex key ---> vertex index in list

    def isEmpty(self):
        return len(self.list) == 0

    def insertVertex(self, vertex):
        if vertex not in self.vertex_list:
            self.list.append({})
            self.vertex_list.append(vertex)
            self.dict[vertex] = self.order() - 1

    def insertEdge(self, vertex1, vertex2, edge=Edge(0)):
        if vertex1 not in self.vertex_list:
            self.insertVertex(vertex1)
        if vertex2 not in self.vertex_list:
            self.insertVertex(vertex2)

        self.list[self.getVertexIdx(vertex1)][vertex2] = edge

    def deleteVertex(self, vertex):
        if vertex in self.vertex_list:
            vertex_idx = self.getVertexIdx(vertex)
            self.list.pop(vertex_idx)
            for dictionary in self.list:
                dictionary.pop(vertex, None)
            self.dict.pop(vertex)
            for idx in range(vertex_idx + 1, self.order()):
                self.dict[self.vertex_list[idx]] = idx - 1
            self.vertex_list.pop(vertex_idx)

    def deleteEdge(self, vertex1, vertex2):
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list:
            self.list[self.getVertexIdx(vertex1)].pop(vertex2)

    def getVertexIdx(self, vertex):
        return self.dict[vertex]

    def getVertex(self, vertex_idx):
        return self.vertex_list[vertex_idx]

    def neighboursIdx(self, vertex_idx):
        return [self.getVertexIdx(key) for key in self.list[vertex_idx].keys()]

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
            result += [(vertex1, vertex2) for vertex2 in dictionary.keys()]
        return result

    def display(self):
        print("--------------------")
        for idx, dictionary in enumerate(self.list):
            vertex1 = self.getVertex(idx)
            print(vertex1, "-", dictionary)
        print("--------------------")


def test(graph_type):
    if graph_type == "Matrix":
        graph = MatrixOfNeighbours()
    elif graph_type == "List":
        graph = ListOfNeighbours()
    else:
        return

    for edge in polska.graf:
        graph.insertEdge(edge[0], edge[1], Edge(1))

    graph.deleteVertex("K")
    graph.deleteEdge("W", "E")
    graph.deleteEdge("E", "W")
    polska.draw_map(graph.edges())


if __name__ == "__main__":

    test("Matrix")

    test("List")

    # matrix = ListOfNeighbours()
    # matrix.insertVertex(Vertex("K"))
    # matrix.insertVertex(Vertex("G"))
    # matrix.insertVertex(Vertex("W"))
    # matrix.insertEdge(Vertex("K"), Vertex("W"), Edge(1))
    # matrix.insertEdge(Vertex("K"), Vertex("G"), Edge(1))
    # matrix.display()
    # print(matrix.size())
    # print(matrix.neighboursIdx(0))
    # print(matrix.edges())
    # matrix.deleteVertex(Vertex("K"))
    # matrix.display()
    # print(matrix.size())
    # print(matrix.neighboursIdx(0))
    # print(matrix.edges())
    # print(matrix.order())

