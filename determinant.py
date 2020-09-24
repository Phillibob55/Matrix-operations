def cofactors(matrix):
    cofactor = [[0,0],[0,0]]
    det = 0
    i = 0
    j = 0
    for exception in range(3):
        cofactor = [[0,0],[0,0]]
        i = 0
        for x in range(1,3):
            j = 0
            for y in range(3):
                if y == exception:
                    continue
                else:
                    cofactor[i][j] = (matrix[x][y])
                    j+=1
            i+=1
        det += determinant(cofactor, 1, exception + 1, matrix[0][exception])
    return det

def determinant(matrix, i = 1 , j = 1,cof = 1):
    sign = (-1)**(i + j)
    det = sign * cof * (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
    return det

if __name__ == "__main__":
    # Format: [[row1],[row2],[row3]]
    # print cofactors(matrix) for 3x3 and print determinant(matrix) for 2x2 matrix
    # For Example, for 3x3:
    matrix = [[2,4,7],[4,7,3],[2,9,1]]
    print(cofactors(matrix))

    # And for 2x2
    matrix2 = [[1,3],[7,9]]
    print(determinant(matrix2))
