from matrix import *


def determinant_chio(matrix: Matrix) -> int:
    if matrix.row != matrix.col:
        raise ValueError("Macierz prostokątna")
    if matrix.row == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        temp_matrix = Matrix((matrix.row-1, matrix.col-1))
        corner = matrix[0][0]
        sign = 1
        if corner == 0:
            for row in range(1, matrix.row):
                if matrix[row][0] != 0:
                    for i in range(matrix.col):
                        temp = matrix[0][i]
                        matrix[0][i] = matrix[row][i]
                        matrix[row][i] = temp
                    sign = -1
                    corner = matrix[0][0]
                    break
        for i in range(1, matrix.row):
            for j in range(1, matrix.col):
                temp_matrix[i-1][j-1] = corner*matrix[i][j] - matrix[0][j]*matrix[i][0]
        return sign*determinant_chio(temp_matrix)/(corner**(matrix.row-2))


def main():
    m1 = Matrix([[5, 1, 1, 2, 3],
                 [4, 2, 1, 7, 3],
                 [2, 1, 2, 4, 7],
                 [9, 1, 0, 7, 0],
                 [1, 4, 7, 2, 2]])

    print(determinant_chio(m1))

    m2 = Matrix([[0, 1, 1, 2, 3],
                 [4, 2, 1, 7, 3],
                 [2, 1, 2, 4, 7],
                 [9, 1, 0, 7, 0],
                 [1, 4, 7, 2, 2]])

    print(determinant_chio(m2))


main()
