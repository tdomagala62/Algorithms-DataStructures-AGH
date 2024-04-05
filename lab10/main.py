
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
    def __init__(self, capacity, isResidual: bool = False):
        self.capacity = capacity
        self.isResidual = isResidual
        if isResidual:
            self.flow = None
            self.residual = 0
        else:
            self.flow = 0
            self.residual = self.capacity

    def __repr__(self):
        return str(self.capacity) + " " + str(self.flow) + " " + str(self.residual) + " " + str(self.isResidual)


class ListOfNeighbours:
    def __init__(self):
        self.list = []          # list of dictionaries - [{1st vertex.key : [Edge, ...]}, {2nd vertex.key : [Edge, ...]}, ...]
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

        if vertex2.key in self.list[self.getVertexIdx(vertex1)].keys():
            self.list[self.getVertexIdx(vertex1)][vertex2.key].append(edge)
        else:
            self.list[self.getVertexIdx(vertex1)][vertex2.key] = [edge]

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


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighboursIdx(i)
        for idx in nbrs:
            for edge in g.list[i][g.vertex_list[idx].key]:
                print(g.getVertex(idx), edge, end=";")
        print()
    print("-------------------")


def load_graph(graf_list):    # WORKED
    graph = ListOfNeighbours()
    for i in graf_list:
        vertex1 = Vertex(i[0])
        vertex2 = Vertex(i[1])
        graph.insertEdge(vertex1, vertex2, Edge(i[2]))
        graph.insertEdge(vertex2, vertex1, Edge(i[2], True))
    return graph


def BFS(graph: ListOfNeighbours, start_vertex_idx):   # WORKED
    visited = graph.order()*[0]
    parent = graph.order()*[float("inf")]
    queue = [start_vertex_idx]
    visited[start_vertex_idx] = 1
    while queue:
        vertex_idx = queue.pop(0)
        neighbours = graph.neighboursIdx(vertex_idx)
        for neighbour_idx in neighbours:
            for edge in graph.list[vertex_idx][graph.vertex_list[neighbour_idx].key]:
                if visited[neighbour_idx] == 0 and edge.residual > 0:
                    queue.append(neighbour_idx)
                    visited[neighbour_idx] = 1
                    parent[neighbour_idx] = vertex_idx
                    # break # Może
    return parent


def analyze_path(graph: ListOfNeighbours, start_vertex_idx, end_vertex_idx, parent):    # WORKED
    current_vertex_idx = end_vertex_idx
    min_capacity = float("inf")
    if parent[current_vertex_idx] == float("inf"):
        return 0
    else:
        while current_vertex_idx != start_vertex_idx:
            for edge in graph.list[parent[current_vertex_idx]][graph.vertex_list[current_vertex_idx].key]:
                if edge.isResidual is False:
                    if edge.residual < min_capacity:
                        min_capacity = edge.residual
                    current_vertex_idx = parent[current_vertex_idx]
    return min_capacity


def aug_path(graph: ListOfNeighbours, start_vertex_idx, end_vertex_idx, parent, min_capacity):    # WORKED
    current_vertex_idx = end_vertex_idx
    while current_vertex_idx != start_vertex_idx:
        for real_edge in graph.list[parent[current_vertex_idx]][graph.vertex_list[current_vertex_idx].key]:
            if real_edge.isResidual is False:
                real_edge.flow += min_capacity
                real_edge.residual -= min_capacity
        for residual_edge in graph.list[current_vertex_idx][graph.vertex_list[parent[current_vertex_idx]].key]:
            if residual_edge.isResidual is True:
                residual_edge.residual += min_capacity
        current_vertex_idx = parent[current_vertex_idx]


def FF_EK(graph: ListOfNeighbours, source_idx, sink_idx):
    parent = BFS(graph, source_idx)
    min_capacity = analyze_path(graph, source_idx, sink_idx, parent)
    while min_capacity > 0:
        aug_path(graph, source_idx, sink_idx, parent, min_capacity)
        parent = BFS(graph, source_idx)
        min_capacity = analyze_path(graph, source_idx, sink_idx, parent)
    sum = 0
    for dictionary in graph.list:
        edges = dictionary.get(graph.vertex_list[sink_idx].key, None)
        if edges:
            for edge in edges:
                sum += edge.flow
    return sum


if __name__ == "__main__":
    graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
    graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9),
              ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
    graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
              ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7),
              ('d', 'c', 4)]

    for graf in [graf_0, graf_1, graf_2, graf_3]:
        graph = load_graph(graf)
        print(FF_EK(graph, graph.getVertexIdx(Vertex('s')), graph.getVertexIdx(Vertex('t'))))
        printGraph(graph)