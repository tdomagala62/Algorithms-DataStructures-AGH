from typing import List, Tuple, Union


class Matrix:
    def __init__(self, _matrix: Union[Tuple[int, int], List[List[int]]], _value=0):
        if isinstance(_matrix, Tuple):
            self.row = _matrix[0]
            self.col = _matrix[1]
            self.__matrix = [_matrix[1] * [_value] for i in range(_matrix[0])]
        else:
            self.__matrix = _matrix
            self.row = len(_matrix)
            self.col = len(_matrix[0])

    def size(self):
        return self.row, self.col

    def __getitem__(self, item):
        return self.__matrix[item]

    def __add__(self, other):
        result = None
        if self.row == other.row and self.col == other.col:
            result = Matrix(self.size())
            for i in range(self.row):
                for j in range(self.col):
                    result[i][j] = self.__matrix[i][j] + other[i][j]
        return result

    def __mul__(self, other):
        result = None
        if self.col == other.row:
            result = Matrix((self.row, other.col))
            for i in range(self.row):
                for j in range(other.col):
                    value = 0
                    for num in range(self.col):
                        value += self.__matrix[i][num]*other[num][j]
                    result[i][j] = value
        return result

    def __str__(self):
        result = ""
        for i in range(self.row):
            result += "|"
            for j in range(self.col):
                result += str(self.__matrix[i][j])
                if j != self.col - 1:
                    result += " "
            result += "|\n"

        return result


def transpose(matrix: Matrix) -> Matrix:
    result = Matrix((matrix.col, matrix.row))
    for i in range(matrix.row):
        for j in range(matrix.col):
            result[j][i] = matrix[i][j]
    return result


if __name__ ==  "__main__":
    m1 = Matrix([[1, 0, 2],
                 [-1, 3, 1]])
    m2 = Matrix((2, 3), 1)
    m3 = Matrix([[3, 1],
                 [2, 1],
                 [1, 0]])
    # 1
    print(transpose(m1))
    # 2
    print(m1+m2)
    # 3
    print(m1*m3)
