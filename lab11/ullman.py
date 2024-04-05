import numpy as np


class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __repr__(self):
        return self.key


class MatrixOfNeighbours:
    def __init__(self):
        self.matrix = []
        self.vertex_list = []  # List of vertex's key
        self.dict = {}         # vertex key ---> vertex index in list
        self.fill = 0

    def isEmpty(self):
        return len(self.matrix) == 0

    def insertVertex(self, vertex: Vertex):
        if vertex not in self.vertex_list:
            self.vertex_list.append(vertex)
            self.dict[vertex] = self.order() - 1
            if self.isEmpty():
                self.matrix.append([self.fill])
            else:
                for row in self.matrix:
                    row.append(self.fill)
                self.matrix.append([self.fill for i in range(self.order())])

    def insertEdge(self, vertex1: Vertex, vertex2: Vertex, edge=0):
        if vertex1 not in self.vertex_list:
            self.insertVertex(vertex1)
        if vertex2 not in self.vertex_list:
            self.insertVertex(vertex2)

        self.matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = edge

    def deleteVertex(self, vertex: Vertex):
        if vertex in self.vertex_list:
            vertex_idx = self.getVertexIdx(vertex)
            self.matrix.pop(vertex_idx)
            for row in self.matrix:
                row.pop(vertex_idx)
            self.dict.pop(vertex)
            for idx in range(vertex_idx + 1, self.order()):
                self.dict[self.vertex_list[idx]] = idx - 1
            self.vertex_list.pop(vertex_idx)

    def deleteEdge(self, vertex1: Vertex, vertex2: Vertex):
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list:
            self.matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = None

    def getVertexIdx(self, vertex: Vertex):
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

    def get_matrix(self):
        return self.matrix


def ullman_v1(current_row, M: np.array, used, G, P, no_recursion):
    if current_row == M.shape[0]:
        if np.array_equal(P, M@((M@G).T)):
            correct_list_v1.append(np.copy(M))
        return no_recursion
    else:
        for i in range(M.shape[1]):
            if used[i] is False:
                used[i] = True
                M[current_row, :] = np.zeros((M.shape[1]))
                M[current_row, i] = 1
                no_recursion = ullman_v1(current_row+1, M, used, G, P, no_recursion)
                no_recursion += 1
                used[i] = False
        return no_recursion


def ullman_v2(current_row, M: np.array, used, G, P, no_recursion):
    if current_row == M.shape[0]:
        if np.array_equal(P, M@((M@G).T)):
            correct_list_v2.append(np.copy(M))
        return no_recursion
    else:
        for i in range(M.shape[1]):
            if used[i] is False and M0[current_row, i] == 1:
                used[i] = True
                M[current_row, :] = np.zeros((M.shape[1]))
                M[current_row, i] = 1
                no_recursion = ullman_v2(current_row+1, M, used, G, P, no_recursion)
                no_recursion += 1
                used[i] = False
        return no_recursion


def prune(M):
    changed = True
    while changed:
        changed = False
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if M[i, j] == 1:
                    neighbours_P = graphP.neighboursIdx(i)
                    neighbours_G = graphG.neighboursIdx(j)
                    has = False
                    for x in neighbours_P:
                        for y in neighbours_G:
                            if M[x, y] == 1:
                                has = True
                                break
                        if has:
                            break
                    if not has:
                        M[i, j] = 0
                        changed = True


def ullman_v3(current_row, M: np.array, used, G, P, no_recursion):
    if current_row == M.shape[0]:
        if np.array_equal(P, M@((M@G).T)):
            correct_list_v3.append(np.copy(M))
        return no_recursion
    else:
        M_copy = np.copy(M)
        prune(M_copy)
        for i in range(M_copy.shape[1]):
            if used[i] is False and M0[current_row, i] == 1:
                used[i] = True
                M_copy[current_row, :] = np.zeros((M_copy.shape[1]))
                M_copy[current_row, i] = 1
                no_recursion = ullman_v3(current_row+1, M_copy, used, G, P, no_recursion)
                no_recursion += 1
                used[i] = False
        return no_recursion


if __name__ == "__main__":
    graphG = MatrixOfNeighbours()
    graphP = MatrixOfNeighbours()

    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

    for i in graph_G:
        graphG.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])
        graphG.insertEdge(Vertex(i[1]), Vertex(i[0]), i[2])

    for i in graph_P:
        graphP.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])
        graphP.insertEdge(Vertex(i[1]), Vertex(i[0]), i[2])

    matrixG = np.array(graphG.get_matrix())
    matrixP = np.array(graphP.get_matrix())
    M = np.zeros((matrixP.shape[0], matrixG.shape[0]))

    correct_list_v1 = []
    correct_list_v2 = []

    M0 = np.zeros((graphP.order(), graphG.order()))
    for i in range(graphP.order()):
        deg_P = np.count_nonzero(matrixP[i, :])
        for j in range(graphG.order()):
            deg_G = np.count_nonzero(matrixG[j, :])
            if deg_P <= deg_G:
                M0[i, j] = 1

    # V1
    correct_list_v1 = []
    used = M.shape[1] * [False]
    iter_v1 = ullman_v1(0, M, used, matrixG, matrixP, 0)
    print(len(correct_list_v1), iter_v1)

    # V2
    correct_list_v2 = []
    used = M.shape[1] * [False]
    iter_v2 = ullman_v2(0, M, used, matrixG, matrixP, 0)
    print(len(correct_list_v2), iter_v2)

    # V3
    correct_list_v3 = []
    used = M.shape[1] * [False]
    iter_v3 = ullman_v3(0, M, used, matrixG, matrixP, 0)
    print(len(correct_list_v3), iter_v3)




